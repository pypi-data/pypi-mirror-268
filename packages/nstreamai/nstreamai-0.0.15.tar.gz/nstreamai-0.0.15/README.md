# ms-public-sdk
![Nstream SDK](images/mermaid-diagram.svg "Nstream SDK")

## Quick Start Guide
### Using the Nstream SDK for Recommending Promotions

### Introduction
The Nstream SDK is designed for building and managing neural network pipelines that incorporate large language models (LLMs) and stream processing capabilities. This guide will walk you through creating a simple but powerful neural network pipeline for generating insights from streaming data using the Nstream SDK.

### Installation

To begin using the Nstream SDK in your projects, install it via pip with the following command:

```bash
pip install nstreamai
```

After installation, import the necessary modules and classes as follows:

```python
from nstreamai_nstream_ai.core.nsinit import NsInit
from nstreamai_nstream_ai.core.nsnode import (
    NsNode, NsLink, NsProvider, NsProviderType, Nstream
)
from nstreamai_nstream_ai.core.nsneuron import NsNeuron, NstreamLLM
from nstreamai_nstream_ai.core.nsgraph import NsGraph
from utils.logger import logger
import sys
```
## Core Module Imports

### NsInit
**Import**: `from nstreamai_nstream_ai.core.nsinit import NsInit`

**Description**: This import brings in the `NsInit` class responsible for initializing and configuring the connection settings for the Nstream SDK.

**Usage**: It is used to set up the initial connection with the Nstream API using credentials like API key, username, and password.

### NsNode, NsLink, NsProvider, NsProviderType, Nstream
**Import**: `from nstreamai_nstream_ai.core.nsnode import NsNode, NsLink, NsProvider, NsProviderType, Nstream`

**Description**: This import includes multiple classes that are fundamental to constructing nodes within an Nstream pipeline:
- **NsNode**: Represents a single node in the neural network graph.
- **NsLink**: Used to define connections between nodes and data sources or sinks.
- **NsProvider**: Specifies the data source or sink type.
- **NsProviderType**: Enumerates different types of data providers.
- **Nstream**: Might be used for additional functionality directly related to stream operations.

**Usage**: These are used to define and link the functional components of a neural network pipeline, such as data inputs, transformations, and outputs.

### NsNeuron, NstreamLLM
**Import**: `from nstreamai_nstream_ai.core.nsneuron import NsNeuron, NstreamLLM`

**Description**: This import involves classes related to the neural network computation units within the SDK:
- **NsNeuron**: Represents a neuron unit which can execute specific neural network computations or models.
- **NstreamLLM**: Pertains to specific large language model configurations that can be deployed within neurons.

**Usage**: These are used to specify and configure the large language models that perform the actual analytics and insights generation in the pipeline.

### NsGraph
**Import**: `from nstreamai_nstream_ai.core.nsgraph import NsGraph`

**Description**: Imports the `NsGraph` class, which manages the execution flow of neural network nodes defined with `NsNode`.

**Usage**: This class is crucial for defining the execution order and dependencies between nodes, as well as starting and stopping the data processing workflow.

### Configuration
Start by initializing the SDK and connecting to the Nstream service:

```python
try:
    logger.info("Starting main execution")
    conn = NsInit(
        api_key="your_api_key", 
        username="your_username", 
        password="your_password").connect()
    logger.info("Connected to NsInit")
except Exception as e:
    logger.exception(
        "Exception occurred while initializing NsInit"
        )
    print(e)
    sys.exit()
```

### Building the Pipeline
#### Node 1: User Interaction Summarization and Insight Generation
Create the first node to summarize user interactions and generate insights:

```python
prompt_event = Nstream.event()
ns_node_1_prompt_text = f"Generate a general insight using a user's data - {prompt_event}"
ns_node_1_context_transform_prompt_text = "Transform unstructured user data into a detailed JSON format..."

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
```

#### Node 2: Personalized Recommendations
Set up the second node to use insights from Node 1 to generate personalized recommendations:

```python
ns_node_2_prompt_text = "Based on general insight, provide a list of recommended promotional offers"
ns_node_2_context_transform_prompt_text = "Transform unstructured promotional data into a structured JSON format..."

ns_node_2 = NsNode(
    node_name="GraphNode2",
    prompt=NsLink(
        socket=conn,
        provider=NsProvider(
            type=NsProviderType().Source).mongodb(),prompt_text=ns_node_2_prompt_text),
    context=ns_node_1.output(
        context_transform_prompt_text=ns_node_2_context_transform_prompt_text),
    neuron=NsNeuron(NstreamLLM.llama2_7b()),
    socket=conn)
logger.info("GraphNode2 configured")
```
#### Running the Pipeline
Execute the configured pipeline and handle the output:
```python
ns_graph_sink = NsLink(socket=conn, provider=NsProvider(type=NsProviderType().Sink).terminal())
logger.info("Graph sink configured")

ns_graph = NsGraph(conn).start(ns_node_1).end(ns_node_2).submit(ns_graph_sink)
logger.info("Graph execution started")

ns_graph.terminate(run_time=6)
logger.info("Graph execution terminated")

print("Execution Completed")
logger.info("Main execution completed")
```

Final code would look like this:
```python
from nstreamai_nstream_ai.core.nsinit import NsInit
from nstreamai_nstream_ai.core.nsnode import NsNode, NsLink, NsProvider, NsProviderType, Nstream
from nstreamai_nstream_ai.core.nsneuron import NsNeuron, NstreamLLM
from nstreamai_nstream_ai.core.nsgraph import NsGraph
from utils.logger import logger
import sys

if __name__ == "__main__":
    try:
        logger.info("Starting main execution")
        conn = NsInit(
            api_key="your_api_key", 
            username="your_username", 
            password="your_password").connect()
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
```

##
### Using the Nstream SDK for Genaration Usage Example

#### Building the Pipeline
##### Node 1: User Interaction Summarization
Create the first node to summarize user interactions:

```python
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
```

#### Running the Pipeline
Execute the configured pipeline and handle the output:
```python
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
    logger.info("Main execution completed")
```

Final Code:
```python

# Import necessary modules from the Nstream SDK and utility libraries
from nstreamai_nstream_ai.core.nsinit import NsInit
from nstreamai_nstream_ai.core.nsnode import NsNode, NsLink, NsProvider, NsProviderType, Nstream
from nstreamai_nstream_ai.core.nsneuron import NsNeuron, NstreamLLM
from nstreamai_nstream_ai.core.nsgraph import NsGraph
from utils.logger import logger
import sys

if __name__ == "__main__":
    try:
        # Initialize logging and connect to the Nstream service
        logger.info("Starting main execution")
        conn = NsInit(
            api_key="your_api_key", 
            username="your_username", 
            password="your_password").connect()
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
    logger.info("Main execution completed")
```

### Using the Nstream SDK for Context transformation Usage Example
In this section, we demonstrate a use case of the Nstream SDK for transforming user data 
into a structured format for analysis and insights.

```python
from nstreamai_nstream_ai.core.nsinit import NsInit
from nstreamai_nstream_ai.core.nsnode import NsNode, NsLink, NsProvider, NsProviderType, Nstream
from nstreamai_nstream_ai.core.nsneuron import NsNeuron, NstreamLLM
from nstreamai_nstream_ai.core.nsgraph import NsGraph
from utils.logger import logger
import sys

if __name__ == "__main__":
    try:
        logger.info("Starting main execution")
        conn = NsInit(
            api_key="your_api_key", 
            username="your_username", 
            password="your_password").connect()
        logger.info("Connected to NsInit")
    except Exception as e:
        logger.exception("Exception occurred while initializing NsInit")
        print(e)
        sys.exit()

    # Node 1: User Data Transformation
    # Context Transformation Prompt:
    ns_node_1_context_transform_prompt_text = "Transform unstructured user data into a detailed JSON format that captures comprehensive user interactions, particularly with promotional activities, and includes other vital user data points like geolocation data, data source, and timestamps."

    ns_node_1 = NsNode(
        node_name="GraphNode1",
        context=NsLink(
            socket=conn,
            provider=NsProvider(type=NsProviderType().Source).mongodb(),
            context_transform_prompt_text=ns_node_1_context_transform_prompt_text),
        neuron=NsNeuron(NstreamLLM.mistral_7b()),
        socket=conn)
    logger.info("GraphNode1 configured")

    ns_graph_sink = NsLink(
        socket=conn,
        provider=NsProvider(type=NsProviderType().Sink).terminal(),
    )
    logger.info("Graph sink configured")

    ns_graph = NsGraph(conn).start(ns_node_1).submit(ns_graph_sink)
    logger.info("Graph execution started")

    ns_graph.terminate(run_time=6)
    logger.info("Graph execution terminated")

    logger.info("Main execution completed")
```
