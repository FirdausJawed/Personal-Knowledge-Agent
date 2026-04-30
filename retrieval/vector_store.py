from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

def create_vector_store(text):
    embeddings = OpenAIEmbeddings()
    
    docs = text.split("\n\n")  
    
    db = FAISS.from_texts(docs, embeddings)
    return db

def retrieve(db, query):
    results = db.similarity_search(query, k=2)
    return [r.page_content for r in results]
