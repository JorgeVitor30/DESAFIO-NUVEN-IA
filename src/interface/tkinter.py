from tkinter import ttk
import tkinter as tk
import uvicorn
import requests


class ConversaGUI:
  """"
  Classe responsável por criar a interface gráfica da conversa com o ChatBot e Fazer a integração com a API.
  """
  def __init__(self, root):
    self.root = root
    self.root.title("Conversa com ChatBot")
    
    self.conversa_frame = tk.Frame(self.root)
    self.conversa_frame.pack(fill=tk.BOTH, expand=True)
    
    largura_janela = 800  
    altura_janela = 600
    self.root.geometry(f"{largura_janela}x{altura_janela}")
    
    
    self.scrollbar = ttk.Scrollbar(self.conversa_frame)
    self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    self.conversa_text = tk.Text(self.conversa_frame, wrap=tk.WORD, yscrollcommand=self.scrollbar.set)
    self.conversa_text.pack(fill=tk.BOTH, expand=True)
    self.scrollbar.config(command=self.conversa_text.yview)
    
    
    mensagens = [
        "Bot Assistente: Olá! Como posso ajudar?"
    ]
    for mensagem in mensagens:
        self.adicionar_mensagem(mensagem)
    
    
    self.entrada_var = tk.StringVar()
    self.entrada_entry = ttk.Entry(self.root, textvariable=self.entrada_var, width=100, font=("Arial", 12))
    self.entrada_entry.pack(fill=tk.BOTH)
    self.entrada_entry.bind("<Return>", self.enviar_mensagem)
    
    self.botao = ttk.Button(self.root, text="Treinar", command=self.acao_botao)
    self.botao.place(relx=1, rely=0, anchor=tk.NE)
    

    self.root.protocol("WM_DELETE_WINDOW", self.fechar_janela)

  def adicionar_mensagem(self, mensagem):
    self.conversa_text.insert(tk.END, mensagem + "\n")
    self.conversa_text.see(tk.END)  

  def enviar_mensagem(self, event=None):
    # ROTA DE QUESTION CHATBOT
    mensagem = self.entrada_var.get()
    self.adicionar_mensagem("Você: " + mensagem)
    
    request = requests.post("http://localhost:8000/desafio/bot", json={"question": mensagem})
    
    self.entrada_var.set("")  
    
    self.adicionar_mensagem("ChatBot: " + request.json()["Chatbot"])
        
  def acao_botao(self):
    # ROTA DE TRAIN CHATBOT
    response = requests.post("http://localhost:8000/desafio/training")
    
  
  def fechar_janela(self):
    # Encerrar a aplicação
    self.root.destroy()
  
  
if __name__ == "__main__":
    root = tk.Tk()
    app = ConversaGUI(root)
    root.mainloop()