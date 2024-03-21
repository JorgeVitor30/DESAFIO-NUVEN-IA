from fastapi import HTTPException, status
from src.robot.chat import chat_bot


def startint_bot():
  return chat_bot()
  

