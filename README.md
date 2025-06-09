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

## Design idea

The main idea is to provide a private search assistant that uses LLMs to interact with plain text robustly and various services to enhance the model context, ontology to express structured knowledge and ground responses.

Ragster is a modular, extensible framework for conducting deep, explainable, and automated research using local or remote language models. It integrates Retrieval-Augmented Generation (RAG), structured context handling, and logic-based reasoning to create a programmable system capable of querying, validating, and synthesizing information across a variety of sources.

At its core, Ragster aspires to:

- Ingest information from diverse formats — including documents (PDF, EPUB, HTML, MD), websites, search results, and APIs.

- Enrich retrieval with metadata and semantics — like provenance, inverse indexing, and knowledge graphs.

- Support structured, auditable reasoning — through ontologies, rule-based inference, and formalized decision strategies.

- Offer multiple interaction layers — from REPL to web UI and REST APIs, with future support for LangChain agents and conversational memory.

- Provide a foundation for deep research workflows — modeling research strategy as an ontology and enabling modular reuse, audit trails, and cross-source validation.

Ragster’s architecture is intentionally open and layered, enabling future growth from a simple terminal-based assistant into a full-blown research agent with logic-aware planning and inference.

See `TODO.md` for details and status of implementation.

---

## Features

- Local LLM support via Ollama (e.g., Mistral, LLaMA 3, Deepseek-R1)
- Vector indexing and retrieval with FAISS
- External metadata mapping for traceable answers
- Modular ingestion layer (PDFs, crawls, search results)
- Easy to extend: reasoning, reranking, hybrid retrieval, UI

- The system is meant to try out the latest openly accessible libraries
- The result should replace previous work in Pitch2Canvas

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
ollama_model: deepseek-r1:8b
ollama_model: deepseek-r1:8b
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

## License

MIT License