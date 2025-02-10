# LlamaRAG-Retrieval-Augmented-Generation-with-ChromaDB-Ollama
# LlamaRAG - Retrieval-Augmented Generation with ChromaDB & Ollama

## Overview
LlamaRAG is a Retrieval-Augmented Generation (RAG) system that leverages **ChromaDB** for vector storage, **Ollama** for LLM inference, and **GTE embeddings** for efficient document retrieval. The project allows users to query a knowledge base extracted from PDFs and get AI-generated responses using **Llama 3**.

## Features
- 📄 **PDF Processing**: Extracts text from PDFs using `PyPDFLoader`.
- 🧩 **Text Chunking**: Splits documents into manageable chunks for better retrieval.
- 🧠 **Embeddings with GTE**: Converts text into dense vector representations using `thenlper/gte-small`.
- 🔍 **ChromaDB for Vector Search**: Stores and retrieves relevant text chunks efficiently.
- 🤖 **Llama 3 via Ollama**: Generates intelligent responses based on retrieved data.

## Installation
### Prerequisites
- Python 3.8+
- Ollama installed ([Download Ollama](https://ollama.com/))
- Anaconda (optional but recommended)

### Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/geeky8/LlamaRAG-Retrieval-Augmented-Generation-with-ChromaDB-Ollama.git
   cd LlamaRAG-Retrieval-Augmented-Generation-with-ChromaDB-Ollama
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Ollama in the background**
   ```bash
   ollama serve
   ```

## Usage
### Load and Process PDFs
1. Place your PDFs in the project directory.
2. Update the `pdf_files` list in `rag_assist.py`.
3. Run the script:
   ```bash
   python rag_assist.py
   ```

### Ask a Question
Modify the `query_rag("your question")` function call in `rag_assist.py` to query the knowledge base.

## Example
```python
response = query_rag("What is formal verification?")
print(response)
```

## Troubleshooting
### 1. **Connection Refused for Ollama**
- Ensure Ollama is running by executing:
  ```bash
  ollama serve
  ```
- If still facing issues, restart your system.

### 2. **Git Push Error (refspec main does not match any)**
Run:
```bash
git branch -m master main
git push -u origin main
```

## Roadmap
- ✅ Support for multiple document formats (PDF, TXT, MD)
- ⏳ Web UI using Streamlit
- ⏳ Fine-tuning Llama for domain-specific knowledge

## License
MIT License. See `LICENSE` for details.

