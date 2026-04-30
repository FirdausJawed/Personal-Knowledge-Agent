from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings


def create_vector_store(documents):
    embeddings = OpenAIEmbeddings()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    texts = []
    metadatas = []

    for doc in documents:
        chunks = splitter.split_text(doc["content"])

        for chunk in chunks:
            texts.append(chunk)
            metadatas.append({
                "title": doc["title"],
                "link": doc["link"]
            })

    db = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
    return db


def retrieve(db, query):
    results = db.similarity_search(query, k=3)

    return [
        {
            "content": r.page_content,
            "title": r.metadata["title"],
            "link": r.metadata["link"]
        }
        for r in results
    ]