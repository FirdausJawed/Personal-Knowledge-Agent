from openai import OpenAI
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def summarize(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Summarize this:\n{text}"}
        ]
    )
    return response.choices[0].message.content
