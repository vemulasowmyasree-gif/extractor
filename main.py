from llm import extractor
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class extractorRequest(BaseModel):
    message: str


@app.post("/extractorend_point")
def extractor_user(user_input: extractorRequest):
    print(user_input.message)
    res = extractor(user_input.message)
    print(res)  
    return {
        "data": res
    }