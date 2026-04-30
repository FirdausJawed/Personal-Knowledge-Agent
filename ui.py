import streamlit as st
from ingestion.medium_loader import load_medium_posts
from retrieval.vector_store import create_vector_store
from agent.agent import run_agent

# ---------------- SETUP ---------------- #
@st.cache_resource
def setup():
    docs = load_medium_posts("https://medium.com/feed/@firdaus-jawed")
    db = create_vector_store(docs)
    return db

db = setup()

# ---------------- UI CONFIG ---------------- #
st.set_page_config(page_title="KnowledgeOS", layout="wide")

st.markdown("""
# Firdaus Medium Notes  

#### This AI is trained on my Medium articles — [Medium blogs](https://medium.com/@firdaus-jawed) 

This AI is trained on my personal articles about Java & Spring Boot, System Design & Backend Interviews, Debugging & Performance, My SDE1 → SDE2 journey  

💡 Ask it to Explain concepts I’ve written about (Java, Springboot, SDE1 -> SDE2) and to summarize my blogs  

""")

# ---------------- CHAT STATE ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT ---------------- #
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- INPUT ---------------- #
prompt = st.chat_input("Ask anything about your knowledge...")

if prompt:
    # show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_agent(prompt, db)
            st.markdown(response)

    # store response
    st.session_state.messages.append({"role": "assistant", "content": response})