from fastapi import HTTPException, status
from src.robot.chat import chat_bot
from src.api.models.question import Question


def startint_bot(body: Question):
  try:
    return chat_bot(body.question)
  except Exception as e:
    return {
      "Chatbot": f"{e}"
    }

