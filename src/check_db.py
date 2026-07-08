import chromadb

client = chromadb.PersistentClient(
    path="../processed_data/chroma_db"
)

collections = client.list_collections()

print("Collections found:")

for collection in collections:
    print(collection.name)