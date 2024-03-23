def verify_pdf_in_txt(target):
  caminho_arquivo = r'pdfs_registered.txt'
  
  with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    if target in conteudo:
      return True
    else:
      return False
    
    
def escrever_arquivo_txt(texto):
  caminho_arquivo = r'pdfs_registered.txt'
  try:
    with open(caminho_arquivo, 'a') as arquivo:
      arquivo.write(f"{texto}\n")
      return True
    
  except FileNotFoundError:
    return False


def write_talking_txt(person, texto):
  caminho_arquivo = 'talking_bot.txt'
  
  with open(caminho_arquivo, 'r') as arquivo:
    arquivo = arquivo.read()
  
  try:
    with open(caminho_arquivo, 'a') as arquivo:
      arquivo.write(f" {person}: {texto}\n")
      return True
  except FileNotFoundError:
    return False  
