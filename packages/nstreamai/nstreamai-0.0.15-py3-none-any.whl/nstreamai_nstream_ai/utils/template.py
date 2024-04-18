import json


def create_node_detail_mutation(name, context_size, prompt_size, prompt, context,
                                total_data_processed, model_name):
    return f"""
    mutation {{
      createNodeDetail(
        name: "{name}"
        contextSize: {context_size}
        promptSize: {prompt_size}
        totalDataProcessed: {total_data_processed}
        neuron: "{model_name}"
        prompt: "{prompt}"
        context: "{context}"
      ) {{
        ... on NodeType {{
          id
          name
          orgId
          userId
          contextSize
          promptSize
          totalDataProcessed
          activeSince
          neuron
        }}
        ... on ErrorType {{
          message
        }}
      }}
    }}
    """


def update_node_detail_mutation(id, name, context_size, prompt_size, prompt, context):
    return f"""
    mutation {{
      updateNodeDetail(
        id: "{id}"
        name: "{name}"
        contextSize: {context_size}
        promptSize: {prompt_size}
        prompt: "{prompt}"
        context: "{context}"
      ) {{
        ... on NodeType {{
          id
          name
          orgId
          userId
          contextSize
          promptSize
        }}
        ... on ErrorType {{
          message
        }}
      }}
    }}
    """


def create_data_detail_mutation(type, node_id, avg_throughput, link_metadata,
                                role):
    link_metadata_str = json.dumps(link_metadata).replace('"', '\\"')
    return f"""
    mutation {{
      createDataDetail(
        type: "{type}"
        nodeId: "{node_id}"
        avgThroughPut: {avg_throughput}
        linkMetadata: "{link_metadata_str}"
        role: "{role}"
      ) {{
        ... on DataType {{
          id
          type
          orgId
          userId
          nodeId
          avgThroughPut
          linkMetadata
        }}
        ... on ErrorType {{
          message
        }}
      }}
    }}
    """


def create_token_detail_mutation(tokens, node_id):
    return f"""
    mutation {{
      createTokenDetail(
        tokens: {tokens}
        nodeId: {node_id}
      ) {{
        ... on TokenDetailType {{
          id
          orgId
          userId
          modelName
          tokens
          nodeId
        }}
        ... on ErrorType {{
          message
        }}
      }}
    }}
    """


def update_token_detail_mutation(id, model_name, tokens):
    return f"""
    mutation {{
      updateTokenDetail(
        id: "{id}"
        modelName: "{model_name}"
        tokens: {tokens}
      ) {{
        ... on TokenDetailType {{
          id
          orgId
          userId
          modelName
          tokens
          nodeId
        }}
        ... on ErrorType {{
          message
        }}
      }}
    }}
    """


def create_io_throughput_mutation(node_id, input_throughput,
                                  output_throughput):
    return f"""
    mutation {{
      createIoThroughput(
        nodeId: {node_id}
        inputThroughput: {input_throughput}
        outputThroughput: {output_throughput}
      ) {{
        ... on IOThroughputType {{
          id
          nodeId
          orgId
          userId
          inputThroughput
          outputThroughput
        }}
        ... on ErrorType {{
          message
        }}
      }}
    }}
    """


def update_io_throughput_mutation(id, input_throughput, output_throughput):
    return f"""
    mutation {{
      updateIoThroughput(
        id: "{id}"
        inputThroughput: {input_throughput}
        outputThroughput: {output_throughput}
      ) {{
        ... on IOThroughputType {{
          id
          nodeId
          orgId
          userId
          inputThroughput
          outputThroughput
        }}
        ... on ErrorType {{
          message
        }}
      }}
    }}
    """


def create_inference_latency_mutation(node_id, llm_inference_speed,
                                      context_retrieval_speed,
                                      total_node_inference_speed):
    return f"""
    mutation {{
      createInferenceLatency(
        nodeId: {node_id}
        llmInferenceSpeed: {llm_inference_speed}
        contextRetrievalSpeed: {context_retrieval_speed}
        totalNodeInferenceSpeed: {total_node_inference_speed}
      ) {{
        ... on InferenceLatencyType {{
          id
          nodeId
          orgId
          userId
          llmInferenceSpeed
          contextRetrievalSpeed
          totalNodeInferenceSpeed
        }}
        ... on ErrorType {{
          message
        }}
      }}
    }}
    """


def update_inference_latency_mutation(id, llm_inference_speed,
                                      context_retrieval_speed,
                                      total_node_inference_speed):
    return f"""
    mutation {{
      updateInferenceLatency(
        id: "{id}"
        llmInferenceSpeed: {llm_inference_speed}
        contextRetrievalSpeed: {context_retrieval_speed}
        totalNodeInferenceSpeed: {total_node_inference_speed}
      ) {{
        ... on InferenceLatencyType {{
          id
          nodeId
          orgId
          userId
          llmInferenceSpeed
          contextRetrievalSpeed
          totalNodeInferenceSpeed
        }}
        ... on ErrorType {{
          message
        }}
      }}
    }}
    """

def create_node_message_mutation(message, node_id, key):
    """
    Constructs a GraphQL mutation string for creating a node message.

    :param message: str - The message content in JSON format.
    :param node_id: int - The ID of the node.
    :param key: int - A unique key associated with the message.
    :return: str - GraphQL mutation string.
    """
    # Convert the dictionary to a JSON string
    message_json = json.dumps(message)

    # Manually escape the double quotes for GraphQL
    message_for_graphql = message_json.replace('"', '\\"')
    
    return f"""
    mutation {{
      createNodeMessage(
        message: "{message_for_graphql}"
        nodeId: {node_id}
        key: {key}
      ) {{
        ... on NodeMessage {{
          id
          createdOn
          key
          message
        }}
        ... on ErrorTypeMessage {{
          __typename
          messages
        }}
      }}
    }}
    """

