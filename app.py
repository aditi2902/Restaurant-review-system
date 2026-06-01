import streamlit as st

from src.loader import load_reviews
from src.vectorstore import create_vectorstore
from src.rag_chain import build_chain

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Restaurant Review AI",
    page_icon="🍕",
    layout="wide"
)

# ----------------------------
# Load Data
# ----------------------------
docs = load_reviews(
    "data/realistic_restaurant_reviews.csv"
)

vectorstore = create_vectorstore(docs)

retriever, llm = build_chain(vectorstore)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:

    st.header("📊 Dataset Info")

    st.metric(
        "Reviews Loaded",
        len(docs)
    )

    st.success("Groq Connected")

# ----------------------------
# Title
# ----------------------------
st.title("🍕 Restaurant Review Intelligence System")

st.markdown(
    "Ask questions about restaurant reviews using Retrieval-Augmented Generation (RAG)."
)

# ----------------------------
# Chat History
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ----------------------------
# Suggested Questions
# ----------------------------
st.subheader("💡 Try Asking")

col1, col2 = st.columns(2)

with col1:

    if st.button("🍕 What do customers think about pizza?"):
        st.session_state.suggested_question = (
            "What do customers think about pizza?"
        )

with col2:

    if st.button("⚠️ What complaints appear most often?"):
        st.session_state.suggested_question = (
            "What complaints appear most often?"
        )

# ----------------------------
# Chat Input
# ----------------------------
question = st.chat_input(
    "Ask about restaurant reviews..."
)

# Handle suggested question
if "suggested_question" in st.session_state:

    question = st.session_state.suggested_question

    del st.session_state.suggested_question

# ----------------------------
# Process Question
# ----------------------------
if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    # Retrieve relevant docs
    retrieved_docs = retriever.invoke(question)

    context = "\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = f"""
    Answer the question using the restaurant reviews below.

    Reviews:
    {context}

    Question:
    {question}
    """

    # LLM response
    response = llm.invoke(prompt)

    answer = response.content

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)

    # Show retrieved reviews
    with st.expander("📄 Source Reviews Used"):

        for i, doc in enumerate(retrieved_docs, start=1):

            st.markdown(f"### Review {i}")

            st.write(doc.page_content)

            st.divider()