Restaurant Review Intelligence System
Overview

Restaurant Review Intelligence System is a Retrieval-Augmented Generation (RAG) application that allows users to interact with restaurant reviews using natural language.

The system uses semantic search to retrieve relevant reviews from a vector database and leverages a Large Language Model (LLM) to generate context-aware answers grounded in the retrieved review data.

Features
Retrieval-Augmented Generation (RAG)
Semantic Search using Embeddings
ChromaDB Vector Database
Groq-powered Llama 3.3 Integration
Interactive Streamlit Chat Interface
Source Review Retrieval
Conversation History
Suggested Questions
Real-time Question Answering
Tech Stack
Frontend
Streamlit
Backend
Python
LangChain
Vector Database
ChromaDB
Embedding Model
sentence-transformers/all-MiniLM-L6-v2
Large Language Model
Groq API
Llama 3.3 70B Versatile
Data Processing
Pandas
Project Structure
local-agent-ai/

├── data/
│   └── realistic_restaurant_reviews.csv
│
├── src/
│   ├── loader.py
│   ├── vectorstore.py
│   └── rag_chain.py
│
├── chroma_db/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

Workflow
1. Data Loading

Restaurant reviews are loaded from a CSV file and converted into LangChain Document objects.

2. Embedding Generation

Each review is transformed into a vector representation using the all-MiniLM-L6-v2 embedding model.

3. Vector Storage

The generated embeddings are stored in ChromaDB for efficient semantic retrieval.

4. Query Processing

The user submits a question through the Streamlit interface.

5. Retrieval

The retriever performs similarity search on the vector database and returns the most relevant reviews.

6. Context Construction

Retrieved reviews are combined into a context block.

7. Response Generation

The context and user query are sent to Groq-hosted Llama 3.3, which generates a grounded answer.

8. Display Results

The generated answer and source reviews are displayed in the Streamlit interface.

Example Questions
What do customers think about pizza?
Which reviews mention slow service?
What complaints appear most often?
Are customers generally satisfied?
Summarize customer feedback.
What are customers saying about the restaurant atmosphere?
Installation
Clone Repository
git clone <repository-url>
cd local-agent-ai
Create Virtual Environment
python -m venv myvenv
source myvenv/bin/activate
Install Dependencies
pip install -r requirements.txt
Configure Environment Variables

Create a .env file:

GROQ_API_KEY=YOUR_GROQ_API_KEY
Run Application
streamlit run app.py