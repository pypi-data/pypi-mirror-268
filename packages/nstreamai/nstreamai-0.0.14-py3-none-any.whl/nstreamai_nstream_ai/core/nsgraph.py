import time
import random
from typing import Dict
from ..core.nsinit import NsSocket
from ..core.nsnode import NsNode, NsLink
from ..utils.variables import generate_synthetic_data, send_graphql_request
from ..utils.template import (
    create_token_detail_mutation, 
    create_io_throughput_mutation, 
    create_inference_latency_mutation,
    create_node_message_mutation
    )
from ..utils.logger import logger
import json
from ..utils.output_data import generate_openai_data


class NsGraph(object):

    def __init__(self, socket: NsSocket) -> None:
        self.graph = list(dict())
        self.socket = socket
        self.current_node = None
        self.last_node = None
        self.list_node_id = []
        logger.info("NsGraph initialized")
        pass

    def start(self, node: NsNode):
        logger.info(f"Starting graph with node {node.node_name}")
        self.current_node = node
        node.process()
        self.list_node_id.append(node.node_id)
        return self

    def next_node(self, node: NsNode):
        logger.info(f"Moving to next node {node.node_name}")
        self.last_node = self.current_node
        self.current_node = node
        self.graph.append(self.node_to_dict(self.current_node))
        node.process()
        self.list_node_id.append(node.node_id)
        return self

    def end(self, node: NsNode):
        logger.info(f"Ending graph with node {node.node_name}")
        self.last_node = self.current_node
        self.current_node = node
        self.graph.append(self.node_to_dict(self.current_node))
        node.process()
        self.list_node_id.append(node.node_id)
        return self

    def submit(self, sink: NsLink):
        logger.info(f"Submitting graph with sink {sink.provider.NsProviderName}")
        self.graph.append({"sink": sink})
        self.socket.call_grpc_endpoint(method=(lambda x: x))
        sink.process_sink(self.list_node_id[-1])
        return self

    def terminate(self, run_time):
        logger.info("Processing graph")
        if run_time:
            self.run_data_out(run_time=run_time)
            payload = json.dumps([int(i) for i in self.list_node_id])
            _ = self.socket.call_rest_endpoint(method="DELETE", route="nodes", payload=payload)
        self.socket.call_grpc_endpoint(method=(lambda x: x))
        return self

    @staticmethod
    def node_to_dict(node: NsNode) -> Dict:
        node_dict = dict()
        return node_dict

    def run_data_out(self, run_time) -> None:
        st = time.time()
        while run_time > 0:
            # Generate synthetic data
            for node_id in self.list_node_id:
                data = generate_synthetic_data()
                mutation = create_token_detail_mutation(data["tokens"],
                                                        node_id)
                _ = send_graphql_request(self.socket.dashboard_server,
                                        self.socket.headers, mutation)

                mutation = create_io_throughput_mutation(node_id,
                                                        data["input_throughput"],
                                                        data["output_throughput"])
                _ = send_graphql_request(self.socket.dashboard_server,
                                        self.socket.headers, mutation)

                mutation = create_inference_latency_mutation(
                    node_id, data["llm_inference_speed"],
                    data["context_retrieval_speed"],
                    data["total_node_inference_speed"])
                _ = send_graphql_request(self.socket.dashboard_server,
                                        self.socket.headers, mutation)
                
            # Example usage
            message = generate_openai_data(oauth_token=self.socket.oauth, endpoint=self.socket.api_server).choices[0].message.content
            key = random.randint(1, 10)
            message = json.loads(message)
            mutation = create_node_message_mutation(message=message, node_id=int(node_id), key=key)
            result = send_graphql_request(
                self.socket.dashboard_server,
                self.socket.headers,
                mutation
                )
            logger.info(result.json())
            logger.info(f"Pushed Output")

            sleep_time = 2
            time.sleep(sleep_time)
            run_time -= sleep_time
            logger.info(f"Processing nstream, time remaining: {run_time}")
        et = time.time()
        logger.info(f"Completed in {et - st} seconds")
