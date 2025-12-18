import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import os

# Load resources once
DATA_PATH = "app/data/cleaned_assessments.csv"
INDEX_PATH = "app/data/shl_faiss.index"

df = pd.read_csv(DATA_PATH)
index = faiss.read_index(INDEX_PATH)
model = SentenceTransformer("all-MiniLM-L6-v2")

#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def recommend_assessments(query: str):
    # 1. Embed query
    query_embedding = model.encode([query])

    # 2. FAISS search
    k = 15
    _, indices = index.search(np.array(query_embedding), k)

    candidates = df.iloc[indices[0]][
        ["name", "url", "test_type"]
    ].to_dict(orient="records")

    # 3. LLM re-ranking
    prompt = f"""
User query:
{query}

Candidate assessments:
{candidates}

Task:
- Select 5 to 10 assessments
- Balance Knowledge & Skills (K) and Personality & Behavior (P)
- Return ONLY JSON:
[
  {{"name": "", "url": ""}}
]
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content