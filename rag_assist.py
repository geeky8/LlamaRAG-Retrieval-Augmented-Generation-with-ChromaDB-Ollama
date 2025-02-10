from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM as Ollama
from langchain.chains import RetrievalQA

class RAGAssist:
    def __init__(self, pdf_files):
        self.pdf_files = pdf_files
        self.docs =  self.load_and_process_pdfs()
        self.lang_docs = [Document(page_content=doc.page_content) for doc in self.docs]
        self.embedding_function = HuggingFaceEmbeddings(model_name =  "thenlper/gte-small")
        self.vector_db = self.create_chroma_db()
        self.llm = Ollama(model="llama3")
        self.retriever = self.vector_db.as_retriever()
        self.qa_chain = RetrievalQA.from_chain_type(self.llm, retriever=self.retriever)

    def load_and_process_pdfs(self):
        documents = []
        for pdf in self.pdf_files:
            loader = PyPDFLoader(pdf)
            documents.extend(loader.load())

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        return text_splitter.split_documents(documents)

    def create_chroma_db(self):
        return Chroma.from_documents(
            documents=self.lang_docs,
            embedding=self.embedding_function,
            persist_directory="chroma_db"
        )

    def query_rag(self, question):
        return self.qa_chain.run(question)

if __name__ == "__main__":
    pdf_files = ["final_report.pdf"]
    rag_assist = RAGAssist(pdf_files)
    question = "What is the main topic of the documents?"
    answer = rag_assist.query_rag(question)
    print(answer)