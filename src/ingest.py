import json
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="../processed_data/chroma_db"
)

# Delete old collection if it exists
try:
    client.delete_collection("resume_collection")
except:
    pass

# Create new collection
collection = client.create_collection(
    name="resume_collection"
)

# Load resumes
with open("../processed_data/resumes.json", "r", encoding="utf-8") as f:
    resumes = json.load(f)

print(f"Found {len(resumes)} resumes")

# Store each resume
for resume in resumes:

    embedding = model.encode(
        resume["content"]
    ).tolist()

    collection.add(
        ids=[str(resume["id"])],
        embeddings=[embedding],
        documents=[resume["content"]],
        metadatas=[{
            "candidate": resume["candidate_name"],
            "file": resume["file_name"]
        }]
    )

print("✅ Embeddings stored successfully!")