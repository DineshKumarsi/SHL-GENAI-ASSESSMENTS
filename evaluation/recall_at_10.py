import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/recommend"

tests = pd.read_csv("evaluation/test_queries.csv")

rows = []
for _, r in tests.iterrows():
    resp = requests.post(API_URL, json={"query": r["query"]})
    recs = resp.json()["recommended_assessments"]

    # recs may be JSON string → handle both cases
    if isinstance(recs, str):
        try:
            import json
            recs = json.loads(recs)
        except:
            recs = []

    top10_names = [x["name"] for x in recs][:10]
    rows.append({
        "query": r["query"],
        "ground_truth": r["ground_truth"],
        "top10": "|".join(top10_names)
    })

pd.DataFrame(rows).to_csv("evaluation/predictions.csv", index=False)
print("predictions.csv created")