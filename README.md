# Ragster -- A RAG testbed

Ragster is a modular, extensible system for conducting deep research using local or remote language models and a number of RAG sources. It integrates Retrieval-Augmented Generation (RAG), structured context handling, and symbolic reasoning to create a programmable system capable of querying, validating, and synthesizing information across a variety of sources. 

Ragster’s architecture is intentionally open and layered, enabling future growth from a simple terminal-based assistant into a full-blown research agent with planning and real deductive reasoning that LLMs currently fail at.

The basic version is simple local document-based RAG on Ollama (Mac). 

More advanced functionality solves a few challenges with today's LLM and RAG systems:

- **Explainability and hallucination busting**: A semantic reasoning extension to the implicit semantics and "simulated" reasoning in LLMs will bring a powerful way to integrate data from other sources, slash hallucinations and allow explainability. This is comparable to neurosymbolic approaches where an explicit representation of the world is kept in addition to a neural one.
- **Confidence values** will give an estimate about how certain responses are. Even without LLM-based hallucinations the available knowledge in the may be contradictory. Measuring confidence is the key to resilient agentic use cases, currently not properly solved in LLM-based frameoworks.
- **Flexible research** strategies generalize deep research to follow a generic task strategy to fulfill a set of objectives. For instance, they can ask back based on confidence. This may be further generalized to full agent workflows.
- **Multilayer interaction** will allow users to give feedback and annotations to improve the models and organize their own documentation, e.g., by marking certain sections.
- **Visualization and analytics displays** are embedded based on structured facts and derived statistics. Such visual modules can be added and called from the chat, e.g., explain a business model with an interactive flow diagram.

Note: Developing this framework further lets LLMs move from center-stage to being one integral part of a multi-source data architecture -- the one that provides its robust features to interact with users as well as to structure and semantically interpret information from unstructured sources. We believe that using LLMs with their global knowledge is best when solving very focused tasks and with a semantically structured context, rather than trying to let LLMs "reason", which has been shown to be unstable at scale (empirically and theoretically). The main idea connected to this to aggregate the actual knowledge in the system in structured data backends and move it "out" of the LLM given enough structured evidence. There are still issues to be solved, but they can be tackled one at a time.

This project should replace previous work in Pitch2Canvas that uses a LLM+semantic approach to analyze documents for a given structure (startup pitch deck) and targets (investment theses) and claims verification (RAG use case). It should become the basis of a powerful and flexible cutting-edge research engine.

# Features

Basic:

- **Local LLM support** via Ollama (e.g., Mistral, LLaMA 3, Deepseek-R1)
- **Vector embedding** for indexing and retrieval with FAISS
- **Modular ingestion**:
  - Documents (PDF, TXT, HTML, Markdown)
  - Specific websites and crawls
  - Search engine results
- The system is:
  - meant to try out the latest openly accessible libraries
  - Easy to extend: reasoning, reranking, hybrid retrieval, UI

Advanced:

- **Metadata and reference support**
  - Manual and automated metadata on provenance / traceable answers (data lineage)
  - Inverted index to store references (cf. perplexity)
  - Annotations at document and chunk level
- **Interactive research**:
  - Generalize deep research to ask back based on confidence
  - Follow a generic task strategy to fulfill a set of objectives
  - Further generalize the research to full agent workflows
- **Advanced input**:
  - Understand tables, images
  - Understand textual and visual DSLs (based on format specifications)
- **Multi-layered output**:
  - Start with CLI
  - Web UI and chat
  - Enhanced output objects
    - References (perplexity style)
    - 😎 Structured diagrams
    - Semantic annotations (including explanations)
    - 😎 Interactive visualizations (following semantic content)
- **User feedback**:
  - Note: Interaction in most LLM frontends is flawed. We 
  - 😎 Annotate prompt texts with semantic hints ("topics") to disambiguate and link to ontology
  - 😎 Annotate chat objects (prompts, responses) for later human reuse ("snippets")
  - 😎 Add correction and feedback metadata on existing responses (model improvement)
  - 😎 Give visual feedback (diagrams; presentations; map to text and diagram location)
- **Neurosymbolic reasoning engine**:
  - Note: Large reasoning models (LRMs) iterate via outer-loop token-stream verifications. We use **true** reasoning.
  - 😎 Logic (deductive) reasoning and probabilistic extensions for query context and response verification
  - 😎 Explain prompts and (symbolic) reasoning path, estimate confidence
  - 😎 Formulation of analysis strategies, generalizing deep research to multi-agent workflows
  - Ontology / knowledge graph management from RAG sources

Moonshot objective: "STeams" moves away from the LLM at the center but handle human interaction with a team of different agents (one being LLM).  STeams is based on more generic flow for interaction between human, structured knowledge in databases, semantic knowledge in ontologies, and LLM implicit knowledge, orchestrated by a strategy. A query is answered with a balance of maximal precision and knowledge in the overal system (given confidence targets).

See `TODO.md` for details and status of implementation.

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