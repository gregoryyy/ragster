# TODO for Ragster


## Features

### Interaction
- [x] **REPL** — Interactive command-line loop for querying the system.
- [ ] **Website / Reflex / Streamlit** — Simple browser UI for wider accessibility.
- [ ] **REST API** — Expose endpoints for external tools and services.

### LLM Integration
- [x] **Ollama** — Use local LLMs like `llama3` for offline inference.
- [ ] **OpenAI API** — Connect to GPT-4/3.5 for higher-quality cloud inference.
- [ ] **Google API** — Use PaLM or Gemini via Google Cloud.

### RAG Interface
- [x] **Embedding Vector DB**
  - [x] **FAISS** — Local fast vector search for retrieval.
- [x] **Documents**
  - [x] **PDF** — Load and parse via `fitz`.
  - [ ] **EPUB** — Extract text from e-book formats.
  - [ ] **HTML** — Strip and clean content from HTML pages.
  - [ ] **MD** — Markdown ingestion with optional metadata parsing.
  - [ ] **Office** — Add support for `.docx`, `.xlsx`, `.pptx` via `python-docx`, etc.
- [ ] **Websites** — Ingest structured and unstructured website content.
- [ ] **Crawls** — Traverse links to collect related content.
- [ ] **Search Engine Results** — Ingest top URLs from Serper or Bing search.
- [ ] **REST Services**
  - [ ] **Weather** — Pull live weather data as external grounding.
  - [ ] **Finance** — Pull stock/market data for analysis.

### Metadata
- [ ] **Inverse Index** — Map words back to source chunks for better grounding.
- [ ] **Provenance** — Track where each fact originated.
- [ ] **Semantics** — Enrich metadata with typed meanings, tags, or schema.

### RAG and Semantics
- [ ] **Knowledge Graph / Ontology / Rules (ABox, TBox, RBox)** — Semantic grounding for retrieved content.
- [ ] **Logic Reasoner** — Deductive engine to verify or chain inferences.
- [ ] **Research Strategy as Ontology** — Encode multi-step research plans semantically.

### Deep Research
- [ ] **Research Strategy** — Declarative multi-phase search/validation flow.
- [ ] **Domain ontology** — Model domain-specific concepts and relations.
- [ ] **Strategy Ontology** - Model research strategy as ontology
- [ ] **Integration of Reference Index** — Add curated source index (like Perplexity's verified links).

### Architecture
- [x] **Configuration (`yaml`, `.env`)** — Flexible setup via files and env vars.
- [ ] **Data Backend** — Centralized storage for ingested, embedded, and labeled data.
- [ ] **Structured v2 (LangChain)** — Optional framework-based abstraction.
  - [ ] **Wiring** — Define chain steps and flows.
  - [ ] **Agent and Tool Integration** — Autonomous orchestration via agents.
  - [ ] **Conversational Memory** — Keep chat history and context.
  - [ ] **LLM Abstraction** — Swap LLMs easily behind a common interface.
- [ ] **Formalizing Interaction: MCP (v3)** — Define Machine–Context–Prompt as a structural reasoning interface.

---

## 🐞 Bugs
- [ ] **(TBD)** — Add known issues as they arise.


