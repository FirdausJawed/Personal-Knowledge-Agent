from retrieval.vector_store import retrieve
from tools.summarizer import summarize
from tools.blog_writer import generate_blog
from openai import OpenAI
import streamlit as st
from openai import OpenAI

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def decide_action(query):
    query = query.lower()

    if "summarize" in query:
        return "summarize"
    elif "blog" in query or "write" in query:
        return "blog"
    else:
        return "rag"


def generate_answer(query, context):
    formatted_context = ""

    sources = set()

    for item in context:
        formatted_context += f"""
        Title: {item['title']}
        Content: {item['content']}
        Link: {item['link']}
        """

        sources.add((item["title"], item["link"]))

    prompt = f"""
    Answer the question using the context below.

    Context:
    {formatted_context}

    Question:
    {query}

    Format:

    Answer:
    <clear structured answer>

    Sources:
    - Title (Link)
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def run_agent(query, db):
    action = decide_action(query)

    context = retrieve(db, query)

    if action == "rag":
        return generate_answer(query, context)

    elif action == "summarize":
        clean_text = "\n".join([item["content"] for item in context])
        return summarize(clean_text)

    elif action == "blog":
        clean_text = "\n".join([item["content"] for item in context])
        return generate_blog(clean_text)