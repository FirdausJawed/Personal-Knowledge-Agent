# 🧠 KnowledgeOS – Personal Knowledge Agent

An **agentic AI system** that uses Retrieval-Augmented Generation (RAG) + tool-based reasoning to answer questions, summarize content, and generate blogs from your personal knowledge base.

---

## 🚀 Overview

KnowledgeOS is a lightweight **AI-powered knowledge assistant** that allows you to:

* 🔍 Ask questions over your own content
* ✂️ Summarize notes or documents
* ✍️ Generate structured blog posts

It combines:

* **Vector search (RAG)** for grounding answers
* **Tool-based agent logic** for dynamic behavior
* **LLM generation** for clean, structured responses

---

## 🧩 Features

### 🔍 1. Knowledge Retrieval (RAG)

* Converts your data into embeddings
* Stores them in a vector database
* Retrieves relevant context for queries
* Generates structured answers using LLM

---

### ✂️ 2. Summarization Tool

* Summarizes retrieved knowledge
* Produces concise and readable outputs

---

### ✍️ 3. Blog Generation Tool

* Uses your knowledge to generate:

  * Introduction
  * Examples
  * Common mistakes
  * Conclusion
* Ideal for technical writing and content creation

---

### 🤖 4. Agent Layer

* Detects user intent
* Routes queries to:

  * Retrieval (RAG)
  * Summarizer
  * Blog generator

---

## 🏗️ System Architecture

```
User Input
   ↓
Streamlit UI
   ↓
Agent (Decision Logic)
   ↓
 ┌───────────────┬───────────────┬────────────────┐
 ↓               ↓               ↓
RAG          Summarizer      Blog Generator
 ↓               ↓               ↓
FAISS DB       LLM Tool        LLM Tool
   ↓
Final Response (LLM)
```

---

## 🛠️ Tech Stack

* Python
* Streamlit (UI)
* LangChain (orchestration)
* FAISS (vector database)
* OpenAI API (LLM + embeddings)

---

## 📂 Project Structure

```
knowledge-agent/
│
├── ui.py
├── app.py
├── requirements.txt
│
├── ingestion/
│   └── load_data.py
│
├── retrieval/
│   └── vector_store.py
│
├── tools/
│   ├── summarizer.py
│   └── blog_writer.py
│
├── agent/
│   └── agent.py
│
└── data/
    └── blogs.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Set OpenAI API Key

#### Option A: Environment Variable

```
export OPENAI_API_KEY="your_api_key"
```

#### Option B: (Recommended for deployment)

Use Streamlit secrets

```
OPENAI_API_KEY = "your_api_key"
```

---

### 5️⃣ Run the app

```
streamlit run ui.py
```

---

## 🧪 Example Queries

* `What is memory leak?`
* `Summarize my debugging notes`
* `Write a blog on Java debugging`

---

## 🧠 How It Works

1. **Data ingestion** → Load and split documents
2. **Embedding** → Convert text into vectors
3. **Storage** → Store in FAISS
4. **Retrieval** → Fetch relevant chunks
5. **Agent decision** → Select action
6. **LLM generation** → Produce final answer

---

## 🔥 Key Highlights

* Combines **RAG + Agent + Tools**
* Reduces hallucinations via grounding
* Extensible architecture
* Deployed as an interactive UI

---

## 🚀 Future Improvements

* Replace rule-based agent with LLM-based decision making
* Add conversational memory
* Enable document uploads
* Add streaming responses
* Convert to multi-agent system

---

## 💬 Interview Pitch

> Built a Personal Knowledge Agent leveraging RAG with a vector database to ground responses in user-specific content. Designed an agent layer that dynamically routes queries to retrieval, summarization, or content generation tools, and deployed it via a Streamlit interface.

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

* OpenAI
* LangChain
* Streamlit
* FAISS

---

## ⭐ If you found this useful

Give it a star ⭐ and feel free to contribute!

---
