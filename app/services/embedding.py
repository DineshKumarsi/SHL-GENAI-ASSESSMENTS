import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_PATH = "app/data/cleaned_assessments.csv"
INDEX_PATH = "app/data/shl_faiss.index"

df = pd.read_csv(DATA_PATH)

df["text"] = (
    df["name"].astype(str) + " " +
    df["test_type"].astype(str) + " " +
    df["duration"].astype(str) + " minutes " +
    "Remote testing " + df["remote_testing"].astype(str) + " " +
    "Adaptive IRT " + df["adaptive_irt"].astype(str)
)

texts = df["text"].tolist()

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts, show_progress_bar=True)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, INDEX_PATH)
print("FAISS index created successfully")