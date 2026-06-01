from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def build_chain(vectorstore):

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    llm = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

    return retriever, llm