from fastapi import HTTPException, status
from src.robot.chat import chat_bot
from src.api.models.question import Question


def startint_bot(body: Question):
  try:
    return chat_bot(body.question)
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail=str(e)
    )

