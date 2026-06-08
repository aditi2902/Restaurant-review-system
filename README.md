<b> Restaurant Review Intelligence System <b> <br>
Overview <br>

Restaurant Review Intelligence System is a Retrieval-Augmented Generation (RAG) application that allows users to interact with restaurant reviews using natural language. <br>

The system uses semantic search to retrieve relevant reviews from a vector database and leverages a Large Language Model (LLM) to generate context-aware answers grounded in the retrieved review data. <br>

<b> Features <b> <br>
Retrieval-Augmented Generation (RAG) <br>
Semantic Search using Embeddings <br>
ChromaDB Vector Database <br>
Groq-powered Llama 3.3 Integration <br>
Interactive Streamlit Chat Interface <br>
Source Review Retrieval <br>
Conversation History <br>
Suggested Questions <br>
Real-time Question Answering <br>
Tech Stack <br>
Frontend <br>
Streamlit <br>
Backend <br>
Python <br>
LangChain <br>
Vector Database <br>
ChromaDB <br>
Embedding Model <br>
sentence-transformers/all-MiniLM-L6-v2 <br>
Large Language Model <br>
Groq API <br>
Llama 3.3 70B Versatile <br>
Data Processing <br>
Pandas <br> 

<b>Project Structure <b> <br>
local-agent-ai/ <br>

├── data/ <br>
│   └── realistic_restaurant_reviews.csv <br>
│ <br>
├── src/ <br>
│   ├── loader.py <br>
│   ├── vectorstore.py <br>
│   └── rag_chain.py <br>
│ <br>
├── chroma_db/ <br>
│ <br>
├── app.py <br>
├── requirements.txt <br>
├── .env <br>
├── .gitignore <br>
└── README.md <br>

Workflow <br>
1. Data Loading <br>

Restaurant reviews are loaded from a CSV file and converted into LangChain Document objects. <br>

2. Embedding Generation <br>

Each review is transformed into a vector representation using the all-MiniLM-L6-v2 embedding model. <br>

3. Vector Storage <br>

The generated embeddings are stored in ChromaDB for efficient semantic retrieval. <br>

4. Query Processing <br>

The user submits a question through the Streamlit interface. <br>

5. Retrieval <br>

The retriever performs similarity search on the vector database and returns the most relevant reviews. <br>

6. Context Construction <br>

Retrieved reviews are combined into a context block. <br>

7. Response Generation <br>

The context and user query are sent to Groq-hosted Llama 3.3, which generates a grounded answer. <br>

8. Display Results <br>

The generated answer and source reviews are displayed in the Streamlit interface. <br>

Example Questions <br>
What do customers think about pizza? <br>
Which reviews mention slow service? <br>
What complaints appear most often? <br>
Are customers generally satisfied? <br>
Summarize customer feedback. <br>
What are customers saying about the restaurant atmosphere? <br>

Installation <br>

Clone Repository <br>
git clone <repository-url> <br>
cd local-agent-ai <br>
Create Virtual Environment <br>
python -m venv myvenv <br>
source myvenv/bin/activate <br>
Install Dependencies <br>
pip install -r requirements.txt <br>
Configure Environment Variables <br>

Create a .env file: <br>

GROQ_API_KEY=YOUR_GROQ_API_KEY <br>
Run Application <br>
streamlit run app.py <br>
