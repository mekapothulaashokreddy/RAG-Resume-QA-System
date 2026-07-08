import chromadb
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Connect to Chroma DB
client = chromadb.PersistentClient(
    path="../processed_data/chroma_db"
)


collection = client.get_collection(
    name="resume_collection"
)


def search_resume(query):

    # Convert question into embedding
    query_embedding = model.encode(query).tolist()


    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )


    return results


if __name__ == "__main__":

    question = input(
        "Ask about candidate: "
    )

    result = search_resume(question)

    print("\nResults:")
    print(result["documents"])