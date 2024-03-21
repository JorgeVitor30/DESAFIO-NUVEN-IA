import uvicorn
from fastapi import APIRouter, Depends
from fastapi import FastAPI
from src.api.controllers.processing import processing_extract_to_training
from src.api.controllers.bot import startint_bot


router = APIRouter(
  prefix="/desafio",
  tags=["desafio"],
)


@router.post("/training")
def process_training():
  return processing_extract_to_training()

@router.post("/bot")
def process_question():
  return startint_bot()
