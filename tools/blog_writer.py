from openai import OpenAI
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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