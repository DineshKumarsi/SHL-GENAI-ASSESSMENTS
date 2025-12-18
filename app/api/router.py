from fastapi import APIRouter
from pydantic import BaseModel
from app.services.recommender import recommend_assessments

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/recommend")
def recommend(req: QueryRequest):
    results = recommend_assessments(req.query)
    return {
        "query": req.query,
        "recommended_assessments": results
    }








# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.services.recommender import recommend_assessments
#
# router = APIRouter()
#
# class QueryRequest(BaseModel):
#     query: str
#
# @router.get("/health")
# def health():
#     return {"status": "healthy"}
#
# @router.post("/recommend")
# def recommend(req: QueryRequest):
#     results = recommend_assessments(req.query)
#
#     # Ensure JSON-safe response
#     return {
#         "recommendations": [
#             {
#                 "name": r.get("name"),
#                 "test_type": r.get("test_type"),
#                 "duration": r.get("duration"),
#                 "remote_testing": r.get("remote_testing"),
#                 "adaptive_irt": r.get("adaptive_irt")
#             }
#             for r in results
#         ]
#     }