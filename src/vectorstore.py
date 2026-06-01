from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def create_vectorstore(docs):
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore=Chroma.from_documents(documents=docs,embedding=embeddings,persist_directory="chroma_db")
    return vectorstore