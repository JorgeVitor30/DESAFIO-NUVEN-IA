from fastapi import FastAPI
from pydantic import BaseModel



class Question(BaseModel):
  """
  Classe responsável por definir a estrutura do json de uma pergunta da requisição.
  """
  question: str
  
