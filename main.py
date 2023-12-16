# backend/main.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get-text")
async def get_text():
    return {"message": "Hello from FastAPI backend!"}
