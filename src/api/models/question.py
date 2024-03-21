from fastapi import FastAPI
from pydantic import BaseModel


class Question(BaseModel):
  question: str
  
