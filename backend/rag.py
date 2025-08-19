from langchain.docstore.document import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough

rag_pipeline = None

def load_documents_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    chunks = text.split('\n\n')
    
    documents = [Document(page_content=chunk) for chunk in chunks if chunk.strip()]
    return documents

def initialize_rag_pipeline():
    """
    Builds and initializes the RAG pipeline from a simple text file.
    """
    global rag_pipeline

    knowledge_base_path = 'backend/kb.txt'
    docs = load_documents_from_txt(knowledge_base_path)

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

    template = """
        You are a helpful fitness assistant. Answer the user's question based on the following context.

            Context:
            {context}

            Question:
            {question}

            Answer:
            """
    prompt = PromptTemplate.from_template(template)

    rag_pipeline = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
    )