import os
from openai import OpenAI
from openai.types.chat import ChatCompletion
from httpx import Client, Headers

def get_openai_api_key(oauth_token:str, api_endpoint:str):
    client = Client()
    headers={
            'Authorization': 'Bearer {0}'.format(oauth_token), 
             'Content-Type': 'application/json'}
    url= api_endpoint+"/get-openapi-key"
    return client.post(headers=headers, url=url, json={}).json()

def generate_openai_data(oauth_token:str, endpoint:str)->ChatCompletion:
    if os.environ.get("OPENAI_KEY"):
        pass
    else:
        oai_key = get_openai_api_key(oauth_token, endpoint).get("key", None)
        os.environ.setdefault("OPENAI_KEY", oai_key)

    client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))

    prompt = """
    Generate synthetic data for promotional offers by detailing each offer's ID, title, description, category, discount, validity dates, and target audience demographics, and format it consistently in JSON for use in recommendation systems.
    """
    return client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)
