SHL GenAI Assessment Recommendation System

Overview

This project builds an end-to-end GenAI (RAG) system that recommends the most relevant SHL assessments for a given hiring requirement or job description.
It uses semantic retrieval (FAISS) with LLM re-ranking, exposes a FastAPI backend, provides a Streamlit UI, and evaluates performance using Recall@10.


---

Architecture

1. Data Cleaning → Clean SHL catalog CSV


2. Embeddings → SentenceTransformers (all-MiniLM-L6-v2)


3. Vector Store → FAISS index


4. Retrieval → Top-K semantic search


5. Re-ranking → LLM (OpenAI)


6. API → FastAPI (/health, /recommend)


7. UI → Streamlit


8. Evaluation → Recall@10




---

Tech Stack

Python

FastAPI, Uvicorn

FAISS

SentenceTransformers

OpenAI API

Streamlit

Pandas, NumPy



---

Project Structure

SHL-GENAI-ASSESSMENTS/
├── app/
│   ├── api/router.py
│   ├── core/config.py
│   ├── data/cleaned_assessments.csv
│   ├── data/shl_faiss.index
│   ├── services/recommender.py
│   └── main.py
├── ui/streamlit_app.py
├── evaluation/
│   ├── test_queries.csv
│   ├── predictions.csv
│   └── recall_at_10.py
├── .env
├── requirements.txt
└── README.md


---

Setup

1. Install dependencies

pip install -r requirements.txt

2. Set environment variable

Create .env:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx


---

Run the Application

Start API

uvicorn app.main:app --reload

Health check:

GET http://127.0.0.1:8000/health

Start UI

streamlit run ui/streamlit_app.py

Open:

http://localhost:8501


---

API Usage

POST /recommend

Request

{
  "query": "Hiring a Java developer with strong communication skills"
}

Response

{
  "recommendations": [
    {"name": "Java Coding Test", "...": "..."},
    {"name": "Personality Questionnaire", "...": "..."}
  ]
}


---

Evaluation

Metric: Recall@10

Measures how often the correct assessment appears in the top-10 recommendations.

Run evaluation

python evaluation/recall_at_10.py

Output

evaluation/predictions.csv

Printed Recall@10 score



---

Results

Recall@10: 0.X (acceptable for RAG-based recommendation)

Demonstrates strong semantic retrieval with LLM re-ranking
