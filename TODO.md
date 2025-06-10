# TODO for Ragster

## Overview

The remote goal of the system is to have a flexible way to research data, using data sources and processing modes with their particular benefits and allow to enrich each side mutually, given the confidence of the sources:

- unstructured data incl. prompts/reponses <--> embedding, LLMs
- semistructured data incl. documents <--> Parsed into structured data, embedding and metadata
- structured data incl. databases <--> Query languages (REST, SQL, Cipher)
- semantic data incl.  <--> Reasoners and Query languages (SPARQL)


## Features

🦕 = Basic functionality
😎 = USP
💪 = Moonshot (and likely USP)

### Interaction

Interact with people and external systems:

- [x] **UI** — Interactive command-line
  - [x] **REPL** — 🦕 Interactive command-line loop for querying the system.
  - [ ] **Website / Reflex / Streamlit** — Simple browser UI for wider accessibility.
  - [ ] **Figures** — 💪 Vector images and drawings embedded in answers.
    - [ ] **Visualization** — 💪 Interactive visualizations (e.g., graphs, Causal Loop Diagrams, Topic Maps).
    - [ ] **Analytics** — 💪 Interactive analytics (quantitative).
  - [ ] **References** — Link back to original sources.
  - [ ] **Explainer** — 💪 Explain reference to concepts for explainability (stored in metadata).
  - [ ] **User feedback** — 😎 Mark model output (stored in metadata).
    - [ ] **User annotations** — 😎 Mark important findings for later reuse. 
    - [ ] **Corrections** — 💪 Adjust output and derive corrective actions on model.
- [ ] **REST API** — Expose endpoints for external tools and services.
- [ ] **MCP API** — Model Context Protocol I/O.

### LLM Integration

Interact with LLMs engines:

- [x] **Ollama** — 🦕 Use local LLMs like `llama3` for offline inference.
- [ ] **External APIs** — Access commercial APIs.
  - [ ] **OpenAI API** — Connect to GPT-4/3.5 for higher-quality cloud inference.
  - [ ] **Anthropic API** — Use Claude.
  - [ ] **Google API** — Use PaLM or Gemini via Google Cloud.
- [ ] **Finetuning** — 💪 Extract domain knowledge (incl. semantics) to finetune existing models.
- [ ] **Semantic extraction** — 💪 Any LLM extensions needed to extract semantics from raw data.

### RAG Interface

Integrate external source data into LLM prompts:

- [x] **Embedding Vector DB**
  - [x] **FAISS** — 🦕 Local fast vector search for retrieval.
  - [ ] **VectorDB Variants** — Advanced embedding.
  - [ ] **Embedding storage** — Cache embedded documents.
- [ ] **RAG Workflows** — Structure of RAG interaction through the interaction cycle between user, LLM and external context.
  - [x] 🦕 Prompt Contextualization: Augment prompt with additional information.
  - [ ] Response Verification: Improve reliability, explainability by checking against external sources.
- [ ] **Extensions**
  - [ ] **MCP semantics** — Wire MCP interaction and explainability.
  - [ ] **Structured external memory** — Structured external knowledge representations (extending DB RAG). 
  - [ ] **Memory management** — Knowledge aquisition and forgetting. 

### Source Ingestion

Ingest data from different sources:

- [x] **Local Files** — 🦕 MacOS first. 
- [ ] **Cloud Storage** — Google Drive first. 
- [ ] **Websites** — Ingest structured and unstructured website content.
- [ ] **Crawls** — Traverse links to collect related content.
- [ ] **Search Engine Results** — Ingest top URLs from Serper or Bing search.
- [ ] **Local full-text index** — Standard search embedded documents.
- [ ] **REST Services**
  - [ ] **Weather** — Pull live weather data as external grounding.
  - [ ] **Finance** — Pull stock/market data for analysis.
  - [ ] **News** — Semistructured news content (consider GDELT).
- [ ] **Structured backends** — Query databases. 
  - [ ] **Relational backends** — Query RDBMS / SQL. 
  - [ ] **NoSQL backends** — Query document and KV stores.
  - [ ] **Knowledge Graph / Ontology / Rules** — Data for semantic grounding for retrieved content (ABox, TBox, RBox). 

### Document Processing

Create content and metadata from raw sources:

- [x] **Format Parsers**
  - [x] **PDF** — 🦕 Load and parse via `fitz`.
  - [ ] **EPUB** — Extract text from e-book formats.
  - [ ] **HTML** — Strip and clean content from HTML pages.
  - [ ] **MD** — Markdown ingestion with optional metadata parsing.
  - [ ] **Office** — Add support for `.docx`, `.xlsx`, `.pptx` via `python-docx`, etc.
- [ ] **Structure Parsers** — Parse document structure
  - [ ] **Logical Structure** — Pages, sections, subdocuments
  - [ ] **Tables** — Parse tables.
  - [ ] **Images** — Extract images.
- [ ] **Extended Structure: Domain-Specific Parsers** — Accommodate structured domain semantics.
  - [ ] **DSLs** — Extract DSLs incl. programming languages, math or table cell grammars.
  - [ ] **Images** — Extract specific image types (like diagrams).
- [ ] **Annotation** — Parser annotations kept in metadata (for provenance and fact checking).

### Metadata and Data Integration

Handle data across sources, incl. metadata and integrated data:

- [ ] **Inverted Index** — Map words back to source documents and chunks for better grounding (Elastic etc.).
- [ ] **Provenance** — 😎 Track where each fact originated.
- [ ] **Semantics** — 😎 Enrich metadata with typed meanings, tags or schema.
- [ ] **Explainability** — 😎 Expose model internals.
- [ ] **Data integration** — Merge data from different sources. 
- [ ] **Data Lake** — Local raw data storage. 

### Reasoning and Semantics

Symbolic reasoning and working with semantics:

- [ ] **Semantic Annotation** — 😎 Extract and embed semantic concepts and relations.
- [ ] **Symbolic Reasoning** — 😎 Symbolic reasoning integration to run or verify inferences.
  - [ ] **Logic Reasoner** — 😎 Deductive engine on logic (OWL DL, FOL etc.).
  - [ ] **Probabilistic Extension** — 😎 Allow for vague facts to accommodated edge cases.
- [ ] **Fact Checking** — 💪 Check LLM output against ground truth.
  - [ ] **Confidence Estimator** — 😎 Assign confidence to a prompt/fact/set of facts.
  - [ ] **Improvement Loop** — 😎 Prone inconfident results, retry strategies (prompt-level).
- [ ] **Research Strategy as Ontology** — 😎 Encode multi-step research plans semantically (session-level).
- [ ] **Ontology Learning** — 💪 Extract ontology from documents (likely integrated with interactive tool).

### Structured Agency and Research

Generalizes deep research and agentic workflows as a multi-phase query and validation flow (extends RAG/MCP flows):

- [ ] **Research Strategy** — Declarative multi-phase search/validation flow.
- [ ] **Domain ontology** — 😎 Model domain-specific concepts and relations.
- [ ] **Strategy Reasoner** - 💪 Goal-oriented researcher executing ontology.
- [ ] **Strategy Ontology** - 💪 Model research strategy as ontology.
- [ ] **Integration of Reference Index** — 😎 Add curated source index (like Perplexity's verified links).

### Architecture

General architectural considerations and decisions (incomplete list):

- [x] **Configuration (`yaml`, `.env`)** — 🦕 Flexible setup via files and env vars.
- [ ] **Data Backend** — Centralized storage for ingested, embedded, and labeled data.
- [ ] **Structured Workflows** — Optional framework-based abstraction (e.g., LangChain).
  - [ ] **Wiring** — Define chain steps and flows.
  - [ ] **Agent and Tool Integration** — Autonomous orchestration via agents.
  - [ ] **Conversational Memory** — Keep chat history and context.
  - [ ] **LLM Abstraction** — Swap LLMs easily behind a common interface.

---

## Bugs
- [ ] **(TBD)** — Add known issues as they arise.


## Information flow patterns

### v2 Multi-stage neurosymbolic flow

Accommodate for integration for integration of symbolic semantics. Feedback loops for model improvement.
Deep research orchestrates a set of parts of this flow (prompt-level), based on the research strategy (session-level). 

| Stage                          | Implement in Ragster as                     |
| ------------------------------ | ------------------------------------------- |
| **Query Understanding**        | Classification modules, pre-query logic     |
| **Contextual Retrieval**       | FAISS vector retrieval                      |
| **Prompt Construction**        | Prompt templates + MCP protocol             |
| **Initial Generation**         | Ollama / OpenAI API calls                   |
| **Verification/Clarification** | Follow-up retrieval loop                    |
| **Fact-checking**              | Structured logic modules (ontology/rules)   |
| **Explanation & Provenance**   | Explicit metadata referencing sources       |
| **User Feedback**              | Annotations stored in metadata DB           |
| **Memory & Knowledge Update**  | Structured external memory and vector store |
| **LLM Improvement**            | Fine-tuning datasets, parameter tuning      |

### v3 Multi-agent flow: STeams -- semantic teams

This moves away from the LLM at the center but handle human interaction with a team of different agents (one being LLM).  STeams is based on more generic flow for interaction between human, structured knowledge in databases, semantic knowledge in ontologies, and LLM implicit knowledge, orchestrated by a strategy. Query is answered with a balance of maximal precision and knowledge in the overal system (given confidence targets).

Agents:

- **Orchestrator Agents**:
  - User interaction
  - Controls of workflow
  - Error handling
- **Parser Agent**: 
  - Disambiguates the user query (“what” vs. “how”, intent, entities)
  - Extracts key parameters (e.g. company=X, metric=ROI)
- **Planner Agent**:
  - Breaks the question into subtasks:
    - “Fetch raw numbers from DB”
    - “Validate definitions via ontology”
    - “Generate narrative explanation via LLM”
- **DB–Query Agent**:
  - Runs precise SQL/GraphQL against your structured store
  - Returns exact values, time series, aggregates
- **Ontology Agent**:
  - Runs SPARQL/OWL inference for semantic relations (e.g., “is subsidiary of”, “risk category”)
  - Returns canonical facts or graph‐patterns
- **LLM Agent**:
  - Fills in gaps, generates prose, handles “fuzzy” reasoning
  - Takes both DB numbers and ontology facts as injected context
- **Synthesizer Agent**:
  - Merges all streams with integration rules:
    - “Always trust DB numbers over LLM hallucinations”
    - “If ontology says X implies Y, annotate claim”
    - Constructs a final narrative + citations
- **Human–in–the–Loop Agent**:
  - Presents draft answer with provenance links
  - Captures corrections or approvals
  - Feeds feedback back to the LLM and metadata/index layers


