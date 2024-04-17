import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('OPEN_API_KEY'),
)

prompt = """
Generate synthetic data for promotional offers by detailing each offer's ID, title, description, category, discount, validity dates, and target audience demographics, and format it consistently in JSON for use in recommendation systems.
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)
