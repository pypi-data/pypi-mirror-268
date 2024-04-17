# Import necessary modules from the Nstream SDK and utility libraries
from core.nsinit import NsInit
from core.nsnode import NsNode, NsLink, NsProvider, NsProviderType, Nstream
from core.nsneuron import NsNeuron, NstreamLLM
from core.nsgraph import NsGraph
from utils.logger import logger
import sys

if __name__ == "__main__":
    try:
        # Initialize logging and connect to the Nstream service
        logger.info("Starting main execution")
        conn = NsInit(api_key="NZ4RPFAF3M0", username="admin@nstream.ai", password="nstream.cloud").connect()
        logger.info("Connected to NsInit")
    except Exception as e:
        # Log any exceptions during initialization and exit
        logger.exception("Exception occurred while initializing NsInit")
        print(e)
        sys.exit()

    # Define Node 1: Summarize user interactions
    # Create the first node to summarize user interactions:
    prompt_event = Nstream.event()
    ns_node_1_prompt_text = f"Generate a general insight using input user's data - {prompt_event}"

    # Configure the node with its necessary components
    ns_node_1 = NsNode(
        node_name="GraphNode1",
        prompt=NsLink(
            socket=conn,
            provider=NsProvider(type=NsProviderType().Source).mongodb(),
            prompt_text=ns_node_1_prompt_text
        ),
        neuron=NsNeuron(NstreamLLM.mistral_7b()),
        socket=conn)
    logger.info("GraphNode1 configured")

    # Configure the sink for the graph output, typically a terminal or logger
    ns_graph_sink = NsLink(
        socket=conn,
        provider=NsProvider(type=NsProviderType().Sink).terminal(),
    )
    logger.info("Graph sink configured")

    # Initialize the graph, start execution, and submit it for processing
    ns_graph = NsGraph(conn).start(ns_node_1).submit(ns_graph_sink)
    logger.info("Graph execution started")

    # Terminate the graph execution after a predefined runtime
    ns_graph.terminate(run_time=6)
    logger.info("Graph execution terminated")

    # Signal completion of the main execution
    print("Execution Completed")
    logger.info("Main execution completed")
