from fastapi import APIRouter
from analyzer import analyze_code

router = APIRouter()

@router.get("/")
def home():
    return {"message": "CodeGuard API is running"}

@router.post("/analyze")
def analyze(code: str):
    issues = analyze_code(code)
    return {"detected_issues": issues}
