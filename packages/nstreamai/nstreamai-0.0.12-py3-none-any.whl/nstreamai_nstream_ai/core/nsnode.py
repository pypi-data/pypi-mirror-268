import json
import random
from ..core.nsinit import NsSocket
from typing import Dict, Optional
from ..core.nsneuron import NsNeuron
from ..utils.variables import send_graphql_request
from ..utils.template import create_node_detail_mutation, create_data_detail_mutation
from ..utils.logger import logger

class NsProviderType():
    Sink: str
    Source = str

    def __init__(self) -> None:
        self.Sink = "SINK"
        self.Source = "SOURCE"
        logger.info("NsProviderType initialized")


class NsDataObject():
    NsProviderName: str
    NsProviderMeta: Dict
    NsProviderType: str

    def __init__(self, ns_provider_name, ns_provider_meta,
                 ns_provider_type) -> None:
        self.NsProviderName = ns_provider_name
        self.NsProviderMeta = ns_provider_meta
        self.NsProviderType = ns_provider_type
        logger.info(f"NsDataObject initialized with provider: {ns_provider_name}")
        pass

    def get(self):
        logger.debug(f"Getting data object for provider: {self.NsProviderName}")
        return self


class NsProvider(object):

    def __init__(self, type: str) -> None:
        self.type = type
        logger.info(f"NsProvider initialized with type: {type}")

    def mongodb(self, **kwargs):
        logger.info("Configuring MongoDB provider")
        return NsDataObject(ns_provider_meta=kwargs,
                            ns_provider_name="MONGODB",
                            ns_provider_type=self.type)

    def postgresql(self, **kwargs):
        logger.info("Configuring PostgreSQL provider")
        return NsDataObject(ns_provider_meta=kwargs,
                            ns_provider_name="POSTGRESQL",
                            ns_provider_type=self.type)

    def terminal(self, **kwargs):
        logger.info("Configuring Terminal provider")
        return NsDataObject(ns_provider_meta=kwargs,
                            ns_provider_name="TERMINAL",
                            ns_provider_type=self.type)

    def nsnode(self, **kwargs):
        logger.info("Configuring Node provider")
        return NsDataObject(ns_provider_meta=kwargs,
                            ns_provider_name="NODE",
                            ns_provider_type=self.type)


class Nstream(object):

    def __init__(self, provider: NsProvider) -> None:
        self.provider = provider
        self.event = "EVENT"
        logger.info("Nstream initialized")
        pass
    
    @staticmethod
    def event()->str:
        return "$EVENT"


class NsLink(Nstream):

    def __init__(self,
                 provider: NsProvider,
                 socket: NsSocket = None,
                 prompt_text: Optional[str] = None,
                 context_transform_prompt_text: Optional[str] = None) -> None:
        self.socket = socket
        self.provider = provider
        self.prompt_text = prompt_text
        self.context_prompt_text = context_transform_prompt_text
        logger.info(f"NsLink initialized with provider: {self.provider.NsProviderName}")
        return super().__init__(provider=self.provider)


    def define_prompt(self):
        logger.debug("Defining prompt for NsLink")
        return "{}: \n {}".format(self.prompt_text, self.event)

    def define_context(self):
        logger.debug("Defining context for NsLink")
        return "{}: \n {}".format(self.context_prompt_text, self.event)

    def process_sink(self, node_id) -> None:
        #  datasink - prompt
        avg_throughput = random.uniform(300, 500)
        provider_name = self.provider.NsProviderName
        link_metadata = {provider_name: "value"}
        data_input = self.provider.NsProviderType
        role = "output"
        prompt_mutation = create_data_detail_mutation(data_input, node_id,
                                                      avg_throughput,
                                                      link_metadata, role)
        _ = send_graphql_request(self.socket.dashboard_server,
                                 self.socket.headers, prompt_mutation)



class NsNode(object):

    def __init__(self,
                 node_name: str,
                 prompt: NsLink,
                 context: NsLink,
                 neuron: NsNeuron,
                 socket: NsSocket = None) -> None:
        self.node_name = node_name
        self.prompt = prompt
        self.context = context
        self.neuron = neuron
        self.socket = socket
        logger.info(f"NsNode initialized with name: {node_name}")

    def output(self, context_transform_prompt_text: Optional[str]):
        logger.info("Creating output for NsNode")
        out = NsLink(provider=NsProvider("SOURCE").nsnode(),
                     context_transform_prompt_text=context_transform_prompt_text)
        return out

    
    def process(self) -> None:
        prompt_size = random.randint(20, 80)
        context_size = random.randint(70, 120)
        total_data_processed = random.randint(5, 20)
        node_mutation = create_node_detail_mutation(self.node_name,
                                                    context_size, prompt_size,
                                                    self.prompt.prompt_text, self.context.context_prompt_text,
                                                    total_data_processed,
                                                    self.neuron.llm)
        response = send_graphql_request(self.socket.dashboard_server,
                                        self.socket.headers, node_mutation)
        self.node_id = json.loads(
            response.text).get("data").get("createNodeDetail").get("id")

        #  datasource - prompt
        avg_throughput = random.randint(300, 500)
        provider_name = self.prompt.provider.NsProviderName
        link_metadata = {provider_name: "value"}
        data_input = self.prompt.provider.NsProviderType
        role = "prompt"
        prompt_mutation = create_data_detail_mutation(data_input, self.node_id,
                                                      avg_throughput,
                                                      link_metadata, role)
        response = send_graphql_request(self.socket.dashboard_server,
                                        self.socket.headers, prompt_mutation)

        #  datasource - context
        avg_throughput = random.randint(300, 500)
        provider_name = self.context.provider.NsProviderName
        link_metadata = {provider_name: "value"}
        data_input = self.context.provider.NsProviderType
        role = "context"
        context_mutation = create_data_detail_mutation(data_input,
                                                       self.node_id,
                                                       avg_throughput,
                                                       link_metadata, role)
        response = send_graphql_request(self.socket.dashboard_server,
                                        self.socket.headers, context_mutation)

        return None
