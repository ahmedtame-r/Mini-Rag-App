# Enterprise Corrective RAG Assistant

An enterprise-ready **Corrective Retrieval-Augmented Generation (CRAG)** system built with **LangChain**, **Chroma Vector DB**, and **Ollama (`qwen2.5:3b`)**.

The pipeline automatically evaluates retrieved context quality, rewrites underperforming user queries, re-retrieves documents, filters verified chunks, and produces grounded answers—eliminating hallucinations and providing explicit source attribution.

---

## 🌟 Key Features & Enhancements

1. **Self-Evaluating Retrieval**:
   - Evaluates retrieved context prior to generation.
   - Detects weak or irrelevant retrieved chunks.

2. **Query Rewriting & Re-Retrieval**:
   - Automatically rewrites low-quality queries to improve search precision.
   - Re-evaluates second-pass retrieval context before generation.

3. **Dynamic In-App Document Ingestion**:
   - Upload `.pdf`, `.docx`, `.txt`, and `.csv` files directly in the Gradio web interface.
   - Re-index vector store dynamically with one click without restarting the server.

4. **Hallucination Prevention & Chunk Filtering**:
   - Generates answers strictly using verified context chunks.
   - Outputs honest fallback (*"I couldn't find enough information in the provided documents."*) when no verified context is found.

5. **Optional Web Search Fallback**:
   - Standard CRAG feature: Option to trigger web search (via DuckDuckGo) if local context remains insufficient after query rewriting.

6. **Execution Trace & Timing Metrics**:
   - Live step-by-step trace showing retrieval, evaluation, rewrite, and generation status.
   - Per-step latency metrics breakdown.

7. **Optimized Performance**:
   - Token limit (`num_predict=64`) for evaluator and query rewriter for fast inference.
   - Model `keep_alive` enabled to eliminate cold-start load delays in Ollama.

---

## 📂 Project Architecture

| File | Description |
| :--- | :--- |
| `ingest.py` | Ingestion engine: document loading, cleaning, text splitting, embedding, Chroma DB persistence, dynamic upload processing, and vector database stats. |
| `rag.py` | Core Corrective RAG pipeline: retrieval, context evaluation, query rewriting, chunk filtering, answer generation, and optional web search fallback. |
| `app.py` | Multi-tab Gradio Web Application UI (`Q&A Assistant`, `Document Ingestion`, `Pipeline Settings`). |
| `requirements.txt` | Python dependencies required for the system. |

---

## 🚀 Quick Start Guide

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Ollama and Pull the Model

Ensure [Ollama](https://ollama.com) is installed and running locally (`http://localhost:11434`), then pull the model:

```bash
ollama pull qwen2.5:3b
```

### 3. Build Vector Database

Place your documents into the `DATA/` folder or upload them later via the Web UI, then run:

```bash
python ingest.py
```

### 4. Launch the Web Application

```bash
python app.py
```

Open the local URL printed in your terminal (default: `http://127.0.0.1:7860`) to interact with the system.

---

## 🔄 Corrective RAG Workflow

$$\text{User Question} \rightarrow \text{Retrieve} \rightarrow \text{Evaluate Context} \rightarrow \left(\text{Rewrite Query} \rightarrow \text{Re-retrieve} \rightarrow \text{Re-evaluate}\right) \rightarrow \text{Generate Answer from Verified Context Only} \rightarrow \text{Return Sources / Honest Fallback}$$
# Mini-Rag-App
