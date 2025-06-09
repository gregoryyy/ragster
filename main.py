from ingest.document_loader import load_pdf
from ingest.utils import chunk_text
from core.embedder import embed
from core.vector_store import VectorStore
from core.query_llm import query_ollama
import os

def initialize_index(pdf_path):
    print(f"Loading PDF: {pdf_path}")
    text = load_pdf(pdf_path)
    chunks = chunk_text(text)
    embeddings = embed(chunks)
    store = VectorStore(dim=embeddings.shape[1])
    store.add(embeddings, [{"text": chunk, "source": pdf_path} for chunk in chunks])
    return store

def chat_loop(store):
    print("\n Ask me anything about the loaded document. Type '.exit' to .quit.\n")
    while True:
        question = input("> ")
        if question.lower() in (".exit", ".quit"):
            print("Bye!")
            break
        q_embedding = embed([question])
        results = store.search(q_embedding)
        context = "\n\n".join([f"[Source: {r['source']}]\n{r['text']}" for r in results])
        answer = query_ollama(context, question)
        print(f"\n {answer}\n")

if __name__ == "__main__":
    pdf_path = "data/sources/example.pdf"
    if not os.path.exists(pdf_path):
        print(f" PDF not found: {pdf_path}")
    else:
        store = initialize_index(pdf_path)
        chat_loop(store)