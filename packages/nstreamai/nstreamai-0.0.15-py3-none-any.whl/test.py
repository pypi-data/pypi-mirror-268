from nstreamai_nstream_ai.core.nsgraph import NsGraph
from nstreamai_nstream_ai.core.nsinit import NsInit
from nstreamai_nstream_ai.core.nsnode import NsNode, NsLink, NsProvider, NsProviderType, Nstream
from nstreamai_nstream_ai.core.nsneuron import NsNeuron, NstreamLLM
from nstreamai_nstream_ai.utils.logger import logger
import sys

if __name__ == "__main__":
    try:
        logger.info("Starting main execution")
        conn = NsInit(api_key="FX2QWLX0EPA", username="steve@amazon.com", password="nstreamisawesome").connect()
        logger.info("Connected to NsInit")
    except Exception as e:
        logger.exception("Exception occurred while initializing NsInit")
        print(e)
        sys.exit()

    #  Node 1: User Interaction Summarization and Insight Generation
    #  Objective: Generate Insight using the raw cookie data and historical summarizes of the user’s interactions with promotions on a website.
    prompt_event = Nstream.event()
    #  Prompt for insight generation
    ns_node_1_prompt_text = f"Generate a general insight using a input user's data - {prompt_event}" # Uses stored structured summary from db
    
    #  Context Transformation Prompt:
    ns_node_1_context_transform_prompt_text = "Transform unstructured user data into a detailed JSON format that captures comprehensive user interactions, particularly with promotional activities, and includes other vital user data points like geolocation data, data source, and timestamps."

    ns_node_1 = NsNode(
        node_name="GraphNode1",
        prompt=NsLink(
            socket=conn,
            provider=NsProvider(type=NsProviderType().Source).mongodb(),
            prompt_text=ns_node_1_prompt_text
        ),
        context=NsLink(
            socket=conn,
            provider=NsProvider(type=NsProviderType().Source).mongodb(),
            context_transform_prompt_text=ns_node_1_context_transform_prompt_text),
        neuron=NsNeuron(NstreamLLM.mistral_7b()),
        socket=conn)
    logger.info("GraphNode1 configured")

    #  Node 2: Personalized Recommendations
    #  Objective: Use the insights from Node1 to generate personalized product recommendations based on the user's interactions with promotions.
    
    #  Prompt for Product Listing
    ns_node_2_prompt_text = "Based on general insight, provide a list the recommended promotional offers"
    
    #  Context Transformation Prompt
    ns_node_2_context_transform_prompt_text = "Transform unstructured promotional data into a structured JSON format for better recommendation accuracy. Include essential details like offer ID, title, discount, and audience criteria. Ensure all offers are consistently formatted to enhance analysis and comparison."

    ns_node_2 = NsNode(
        node_name="GraphNode2",
        prompt=NsLink(
            socket=conn,
            provider=NsProvider(type=NsProviderType().Source).mongodb(),
            prompt_text=ns_node_2_prompt_text,
        ),
        context=ns_node_1.output(
            context_transform_prompt_text=ns_node_2_context_transform_prompt_text),
        neuron=NsNeuron(NstreamLLM.llama2_7b()),
        socket=conn)
    logger.info("GraphNode2 configured")

    ns_graph_sink = NsLink(
        socket=conn,
        provider=NsProvider(type=NsProviderType().Sink).terminal(),
    )
    logger.info("Graph sink configured")

    ns_graph = NsGraph(conn).start(ns_node_1).end(ns_node_2).submit(ns_graph_sink)
    logger.info("Graph execution started")

    ns_graph.terminate(run_time=6)
    logger.info("Graph execution terminated")

    logger.info("Main execution completed")
