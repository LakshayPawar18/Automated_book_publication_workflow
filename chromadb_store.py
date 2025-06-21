# === chromadb_store.py ===
import chromadb
from chromadb.config import Settings
from datetime import datetime

client = chromadb.Client(Settings())
collection = client.get_or_create_collection("book_versions")

def save_version(role, version_text):
    timestamp = datetime.now().isoformat()
    doc_id = f"{role}_{timestamp}"
    collection.add(
        documents=[version_text],
        ids=[doc_id],
        metadatas=[{"role": role, "timestamp": timestamp}]
    )
    print(f"Saved version: {doc_id}")

def retrieve_versions():
    return collection.get()