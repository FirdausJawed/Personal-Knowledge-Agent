import streamlit as st
from ingestion.load_data import load_data
from retrieval.vector_store import create_vector_store
from agent.agent import run_agent

# Load data once
@st.cache_resource
def setup():
    text = load_data("data/blogs.txt")
    db = create_vector_store(text)
    return db

db = setup()

st.set_page_config(page_title="Knowledge Agent", layout="wide")

st.title("🧠 Personal Knowledge Agent")
st.write("Ask questions, summarize, or generate blogs from your knowledge.")

# Input box
query = st.text_input("Enter your question:")

if st.button("Run Agent"):
    if query:
        with st.spinner("Thinking..."):
            response = run_agent(query, db)
        
        st.subheader("Response:")
        st.markdown(response)
    else:
        st.warning("Please enter a query.")