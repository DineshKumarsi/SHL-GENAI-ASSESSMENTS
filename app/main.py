from fastapi import FastAPI
from app.api.router import router

app = FastAPI(title="SHL GenAI Assessment Recommendation API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "SHL GenAI API is running"}
