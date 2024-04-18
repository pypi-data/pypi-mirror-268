import json
import random
import string
import requests


def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_json():
    return json.dumps({
        random_string(5): random_string(5)
        for _ in range(random.randint(1, 1))
    })


def generate_synthetic_data():
    tokens = random.randint(10, 300)
    input_throughput = random.randint(50, 500)
    output_throughput = random.randint(50, 500)
    llm_inference_speed = random.randint(10, 800)
    context_retrieval_speed = random.randint(10, 300)
    total_node_inference_speed = llm_inference_speed + context_retrieval_speed + random.randint(
        10, 100)

    return {
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
