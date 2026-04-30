from openai import OpenAI
from openai import OpenAI
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def generate_blog(context):
    prompt = f"""
    Write a structured blog using this context:
    
    {context}
    
    Include:
    - Introduction
    - Examples
    - Common mistakes
    - Conclusion
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content