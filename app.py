
import streamlit as st
import pandas as pd
import plotly.express as px

from src.loader import load_reviews
from src.vectorstore import create_vectorstore
from src.rag_chain import build_chain
from src.sentiment import get_sentiment

st.set_page_config(
    page_title="Restaurant Review AI",
    page_icon="🍕",
    layout="wide"
)

docs = load_reviews(
    "data/realistic_restaurant_reviews.csv"
)

df = pd.read_csv(
    "data/realistic_restaurant_reviews.csv"
)

df["Sentiment"] = df["Review"].apply(
    get_sentiment
)

vectorstore = create_vectorstore(docs)

retriever, llm = build_chain(vectorstore)

positive_count = len(
    df[df["Sentiment"] == "Positive"]
)

negative_count = len(
    df[df["Sentiment"] == "Negative"]
)

neutral_count = len(
    df[df["Sentiment"] == "Neutral"]
)

with st.sidebar:

    st.header("📊 Dataset Info")

    st.metric(
        "Reviews Loaded",
        len(docs)
    )

    st.metric(
        "Positive Reviews",
        positive_count
    )

    st.metric(
        "Negative Reviews",
        negative_count
    )

    st.metric(
        "Neutral Reviews",
        neutral_count
    )

    st.success("Groq Connected")

st.title("🍕 Restaurant Review Intelligence System")

st.markdown(
    """
    Ask questions about restaurant reviews using
    Retrieval-Augmented Generation (RAG).
    """
)

tab1, tab2 = st.tabs(
    [
        "💬 Chat",
        "📈 Analytics"
    ]
)

with tab1:

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    st.subheader("💡 Try Asking")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🍕 What do customers think about pizza?"
        ):
            st.session_state.suggested_question = (
                "What do customers think about pizza?"
            )

    with col2:

        if st.button(
            "⚠️ What complaints appear most often?"
        ):
            st.session_state.suggested_question = (
                "What complaints appear most often?"
            )

    question = st.chat_input(
        "Ask about restaurant reviews..."
    )

    if "suggested_question" in st.session_state:

        question = (
            st.session_state.suggested_question
        )

        del st.session_state.suggested_question

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.write(question)

        retrieved_docs = retriever.invoke(
            question
        )

        context = "\n".join(
            [
                doc.page_content
                for doc in retrieved_docs
            ]
        )

        prompt = f"""
        Answer the question using the restaurant reviews below.

        Reviews:
        {context}

        Question:
        {question}
        """

        response = llm.invoke(prompt)

        answer = response.content

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):
            st.write(answer)

        with st.expander(
            "📄 Source Reviews Used"
        ):

            for i, doc in enumerate(
                retrieved_docs,
                start=1
            ):

                st.markdown(
                    f"### Review {i}"
                )

                st.write(
                    doc.page_content
                )

                st.divider()

with tab2:

    st.subheader(
        "📊 Sentiment Distribution"
    )

    sentiment_counts = (
        df["Sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment_counts.columns = [
        "Sentiment",
        "Count"
    ]

    fig = px.pie(
        sentiment_counts,
        names="Sentiment",
        values="Count",
        title="Review Sentiment Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "😊 Some Positive Reviews"
    )

    positive_reviews = df[
        df["Sentiment"] == "Positive"
    ]

    for review in (
        positive_reviews["Review"]
        .head(5)
    ):
        st.success(review)

    st.subheader(
        "😞 Some Negative Reviews"
    )

    negative_reviews = df[
        df["Sentiment"] == "Negative"
    ]

    for review in (
        negative_reviews["Review"]
        .head(5)
    ):
        st.error(review)

