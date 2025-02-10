# LlamaRAG-Retrieval-Augmented-Generation-with-ChromaDB-Ollama

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

