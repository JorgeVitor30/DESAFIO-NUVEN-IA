from PyPDF2 import PdfReader
from fastapi import HTTPException, status
from src.extraction.extract import Extract
from src.extraction.validate import Validate
from src.utils.functions.open_pdf import opening_pdf_names
from src.utils.functions.transform_csv import transform_csv
from src.utils.functions.open_txt import verify_pdf_in_txt, escrever_arquivo_txt
from src.utils.functions.adding_columns import adding_columns
from src.api.controllers.processing_aux import fill_all_jsons_responses
from src.robot.train import train_bot


def processing_extract_to_training():
  nomes_arquivos_pdfs = opening_pdf_names()

  for nome in nomes_arquivos_pdfs:
    if '.pdf' not in nome:
      continue
    if verify_pdf_in_txt(nome):
      raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="O bot já passou pela extração dos PDFs e treinamento NLP")

    escrever_arquivo_txt(nome)
      
    # EXTRAÇÃO DOS PDFs
    pdf = PdfReader(f'src\\utils\\pdfs\\{nome}')
    extraction = Extract(pdf)
    infos = extraction.extract_text()
    
    # TRATAMENTOS E VALIDAÇÕES
    validation =  Validate(infos)
    infos_formatted = validation.all_validations()
    adding_columns(infos_formatted)
    
    # TRANSFORMAÇÃO PARA CSV
    transform_csv(infos)
  
  # POPULAR OS JSONs
  fill_all_jsons_responses()
  
  train_bot()


  return {
  "detail": "Extração das informações e treinamento do Bot concluída com sucesso"} 