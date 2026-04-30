from ingestion.load_data import load_data
from retrieval.vector_store import create_vector_store
from agent.agent import run_agent

if __name__ == "__main__":
    text = load_data("data/blogs.txt")
    db = create_vector_store(text)

    while True:
        query = input("\nAsk something: ")
        response = run_agent(query, db)
        print("\nResponse:\n", response)
        