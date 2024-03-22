from src.interface.tkinter import ConversaGUI
from fastapi import FastAPI
from src.api.routers.bot import router as router_question
from threading import Thread
import tkinter as tk
import uvicorn


def run_api():
  app = FastAPI()
  
  @app.get("/")
  def index():
    return {"details": "Hello World!"}
  
  app.include_router(router_question)
  
  uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
  fastapi_thread = Thread(target=run_api)
  fastapi_thread.start()
  
  root = tk.Tk()
  app = ConversaGUI(root)
  root.mainloop()

  