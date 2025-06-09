# Ragster = RAG testbed

This project is a modular, extensible **Retrieval-Augmented Generation (RAG)** system that runs entirely locally using:

- **Ollama** for LLM inference
- **FAISS** for vector search
- **Metadata and citation support**
- ...
- Modular ingestion from:
  - Documents (PDF, TXT, HTML, Markdown)
  - Specific websites and crawls
  - Search engine results (Serper, Brave, etc.)
- CLI-based chat (web UI later)
- Optional logic engine:
  - Symbolic reasoning
  - Formulation of analysis strategies

---

## 🚀 Features

- Local LLM support via Ollama (e.g., Mistral, LLaMA 3, Deepseek-R1)
- Vector indexing and retrieval with FAISS
- External metadata mapping for traceable answers
- Modular ingestion layer (PDFs, crawls, search results)
- Easy to extend: reasoning, reranking, hybrid retrieval, UI

---

## Setup Instructions

### 1. Clone Repository

```
gh repo clone gregoryyy/ragster
```


### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure

Edit configuration file `config.yaml`.

Edit `.env`, which overrides any values from config.yaml:

```
SEARCH_API_KEY=<key>
```

Or export manually:

```bash
export SEARCH_API_KEY=<key>
```

### 5. Start Ollama

Install Ollama and start the server:

```bash
homebrew install ollama
ollama serve
``` 

Set the model in `config.yaml`, e.g.:

```yaml
model: deepseek-r1:8b
```

Models see https://ollama.com/

### 6. Start the CLI Chat Interface

```bash
python main.py
```

---

## Structure Overview

```
rag-pipeline/
├── core/            # Embedding, FAISS, Ollama query, logic engine
├── ingest/          # Loaders: PDF, web crawler, search results
├── cli/             # Terminal-based chat
├── data/            # Sources, FAISS index, metadata
├── main.py          # Entry point
├── config.yaml      # Model and retrieval settings
├── .env             # API keys and configs
├── requirements.txt # Python dependencies
```

---

## TODO


---

## License

MIT License