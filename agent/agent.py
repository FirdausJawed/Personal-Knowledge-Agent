from retrieval.vector_store import retrieve
from tools.summarizer import summarize
from tools.blog_writer import generate_blog
from openai import OpenAI
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def decide_action(query):
    query = query.lower()

    if "summarize" in query:
        return "summarize"
    elif "blog" in query or "write" in query:
        return "blog"
    else:
        return "rag"


def generate_answer(query, context):
    joined_context = "\n".join(context)

    prompt = f"""
    Answer the question using the context below.

    Context:
    {joined_context}

    Question:
    {query}

    Format your response as:

    Answer:
    <clear, structured answer>

    Sources:
    - short references from context
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def run_agent(query, db):
    action = decide_action(query)

    # always retrieve context first
    context = retrieve(db, query)

    if action == "rag":
        return generate_answer(query, context)

    elif action == "summarize":
        return summarize("\n".join(context))

    elif action == "blog":
        return generate_blog("\n".join(context))