# Firdaus Medium Notes

A simple AI-powered app that answers questions based on my Medium blogs.

Instead of generic LLM responses, this app retrieves context from my own articles and uses that to generate answers, summaries, and blog drafts.

---

## What this does

- Answers questions asked based on my Medium blog content
- Summarize my medium blogs
- Uses RAG (Retrieval-Augmented Generation) to reduce hallucinations

---

## How it works

1. Fetches blog data (RSS / local content)
2. Splits content into chunks
3. Stores embeddings using FAISS
4. Retrieves relevant chunks for a query
5. Uses OpenAI to generate grounded responses

---

## Tech Stack

- Python
- Streamlit (UI)
- LangChain
- FAISS (vector store)
- OpenAI API

---

## Run locally

```bash
git clone https://github.com/FirdausJawed/Personal-Knowledge-Agent.git
cd Personal-Knowledge-Agent
pip install -r requirements.txt
