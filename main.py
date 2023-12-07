from llama_model import get_response
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"response": "OK"}


@app.get("/response/{question}")
def read_item(question: str):
    print(question)
    response = get_response(question)
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
