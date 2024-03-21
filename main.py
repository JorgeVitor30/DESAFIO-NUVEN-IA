from fastapi import FastAPI
from src.api.routers.bot import router as router_question

app = FastAPI()

@app.get("/")
def index():
  return {"details": "Hello World!"}


app.include_router(router_question)