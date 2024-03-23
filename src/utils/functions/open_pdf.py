import os


def opening_pdf_names():
  
  pasta_pdsf = r'src\\utils\\pdfs\\'
  nomes_arquivos = []
  
  for root, dirs, files in os.walk(pasta_pdsf):
    for file in files:
      nomes_arquivos.append(file)
      
  return nomes_arquivos