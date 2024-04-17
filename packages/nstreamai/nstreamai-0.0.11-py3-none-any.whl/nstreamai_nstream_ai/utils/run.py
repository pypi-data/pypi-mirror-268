import json
import random
import string
import requests
from template import (create_node_detail_mutation,
                      create_token_detail_mutation,
                      create_io_throughput_mutation,
                      create_inference_latency_mutation,
                      create_data_detail_mutation)


def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_json():
    return json.dumps({
        random_string(5): random_string(5)
        for _ in range(random.randint(1, 1))
    })


def generate_synthetic_data():
    model_names = ["Mistral-7B", "LLAMA2-7B"]  # List of model names
    model_name = random.choice(model_names)
    tokens = random.randint(50, 500)
    input_throughput = random.uniform(50, 1000)
    output_throughput = random.uniform(50, 1000)
    llm_inference_speed = random.uniform(10, 5000)
    context_retrieval_speed = random.uniform(10, 5000)
    total_node_inference_speed = llm_inference_speed + context_retrieval_speed + random.uniform(
        10, 100)

    return {
        "model_name": model_name,
        "tokens": tokens,
        "input_throughput": input_throughput,
        "output_throughput": output_throughput,
        "llm_inference_speed": llm_inference_speed,
        "context_retrieval_speed": context_retrieval_speed,
        "total_node_inference_speed": total_node_inference_speed
    }


def send_graphql_request(url, headers, mutation):
    payload = json.dumps({"query": mutation})
    response = requests.post(url, headers=headers, data=payload)
    return response


url = "http://0.0.0.0:8000/graphql"
headers = {
    'Content-Type':
    'application/json',
    'Authorization':
    'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwaXl1c2hAbnN0cmVhbS5haSIsImV4cCI6MTcxNzc0MTcwNn0.DOvgE2BkG9-tqme2DjfH171Kb4vKH-Yb6v2TINhnCqU'
}

node_id_list = []

#  Node 1
node_name = f"Node 1"
prompt_size = random.uniform(20, 80)
context_size = random.uniform(70, 120)
total_data_processed = random.randint(5, 20)
model_name = "Mistral-7B"
mutation = create_node_detail_mutation(node_name, context_size, prompt_size,
                                       total_data_processed, model_name)
response = send_graphql_request(url, headers, mutation)
print(response.text)
node_id = json.loads(
    response.text).get("data").get("createNodeDetail").get("id")
node_id_list.append(node_id)

#  datasource - prompt
avg_throughput = random.uniform(300, 500)
link_metadata = {"S3": "value"}
data_input = "datasource"
role = "prompt"
mutation = create_data_detail_mutation(data_input, node_id, avg_throughput,
                                       link_metadata, role)
response = send_graphql_request(url, headers, mutation)

#  datasource - context
avg_throughput = random.uniform(300, 500)
link_metadata = {"S3": "value"}
data_input = "datasource"
role = "context"
mutation = create_data_detail_mutation(data_input, node_id, avg_throughput,
                                       link_metadata, role)
response = send_graphql_request(url, headers, mutation)

#  Node 2
node_name = f"Node 2"
prompt_size = random.uniform(20, 80)
context_size = random.uniform(70, 120)
total_data_processed = random.randint(5, 20)
model_name = "LLAMA2-7B"
mutation = create_node_detail_mutation(node_name, context_size, prompt_size,
                                       total_data_processed, model_name)
response = send_graphql_request(url, headers, mutation)
print(response.text)
node_id = json.loads(
    response.text).get("data").get("createNodeDetail").get("id")
node_id_list.append(node_id)

#  datasource - prompt
avg_throughput = random.uniform(300, 500)
link_metadata = {"S3": "value"}
data_input = "datasource"
role = "prompt"
mutation = create_data_detail_mutation(data_input, node_id, avg_throughput,
                                       link_metadata, role)
response = send_graphql_request(url, headers, mutation)

#  datasource - context
avg_throughput = random.uniform(300, 500)
link_metadata = {"S3": "value"}
data_input = "datasource"
role = "context"
mutation = create_data_detail_mutation(data_input, node_id, avg_throughput,
                                       link_metadata, role)
response = send_graphql_request(url, headers, mutation)

#  datasink
avg_throughput = random.uniform(300, 500)
link_metadata = {"S3": "value"}
data_input = "datasink"
role = "output"
mutation = create_data_detail_mutation(data_input, node_id, avg_throughput,
                                       link_metadata, role)
response = send_graphql_request(url, headers, mutation)

try:
    while True:
        # Generate synthetic data
        data = generate_synthetic_data()
        data["node_id"] = random.choice(node_id_list)

        mutation = create_token_detail_mutation(data["tokens"],
                                                data["node_id"])
        response = send_graphql_request(url, headers, mutation)

        mutation = create_io_throughput_mutation(data["node_id"],
                                                 data["input_throughput"],
                                                 data["output_throughput"])
        response = send_graphql_request(url, headers, mutation)

        mutation = create_inference_latency_mutation(
            data["node_id"], data["llm_inference_speed"],
            data["context_retrieval_speed"],
            data["total_node_inference_speed"])
        response = send_graphql_request(url, headers, mutation)

except KeyboardInterrupt:
    print("Loop interrupted by user.")
