import re
import datetime
import pandas

from PyPDF2 import PdfReader
from src.extraction.regex import Regex
from src.utils.functions.split_big_string import split_string
from src.utils.functions.remove_accent import remove_accent


class Extract:
  def __init__(self, pdf: PdfReader):
    self.pdf = pdf
    self.pages = len(pdf.pages)
    self.infos = []

  def extract_text(self):
    dict_company = dict()
    
    for i in range(self.pages):
      text = self.pdf.pages[i].extract_text()
      text = remove_accent(text).lower()

      rgx = Regex(text)
      
      if 'nome de pregao' in text and 'codigos de negociacao' in text:
        # DATA DE ATUALIZAÇÃO PDF
        content, error = rgx.match([r'atualizado em\s*(.*?),\s'], 1)
        data_att_pdf = error if error else content[0]
        
        
        # NOME PREGÃO
        content, error = rgx.match([r'nome de pregao:\s*(.*?)\n', r'pregao:\s*(.*?)\n'], 1)
        nome_pregao = (error if error else content[0]).upper()
                 
        # CODIGO NEGOCIAÇÃO
        content, error = rgx.match([r'codigos de negociacao:\s*(.*?)\s+cnpj'], 1)
        cod_negociacao = error if error else content[0]
        
        cod_negociacao = cod_negociacao.split()[2].replace(';', '').upper()
        
        # CNPJ
        content, error = rgx.match([r'cnpj:\s*(.*?)\s', r'npj:\s*(.*?)\s'], 1)
        cnpj = error if error else content[0]

        # CLASSIFICAÇÃO SETORIAL
        content, error = rgx.match([r'classificação setorial:\s*(.*?)\n', r'setorial:\s*(.*?)\n'], 1)
        classi_setor = error if error else content[0]
        
        # SITE  
        content, error = rgx.match([r'site:\s*(.*?)\n'], 1)
        site = error if error else content[0]
        
        dict_company['DataAttPDF'] = data_att_pdf
        dict_company['NomePregao'] = nome_pregao
        dict_company['CodNegociacao'] = cod_negociacao
        dict_company['CNPJ'] = cnpj
        dict_company['CassifSetor'] = classi_setor
        dict_company['Site'] = site
                 
        
      elif 'balanco patrimonial' in text:
        # DATAS DE ATUALIZAÇÃO
        
        content, error = rgx.match([r'balanço patrimonial - consolidado\s*([\d/]+)\s*([\d/]+)', r'consolidado\s*([\d/]+)\s*([\d/]+)'], 2)
        atual_atlz = error if error else content[0]
        ultima_atlz = error if error else content[1]
          
        dict_company['DatAtualAtlz'] = atual_atlz
        dict_company['DatUltimAtlz'] = ultima_atlz

         
        # ATIVO IMOBILIZADO
        content, error = rgx.match([r'ativo imobilizado, investimentos e intangivel\s*(.*?)\n', r'intangivel\s*(.*?)\n'], 1)
        ativo_imob = error if error else content[0]
        
        
        list_ativos = ativo_imob.split(' ')
        ativo_imob_atualizado = list_ativos[0] if len(list_ativos) >= 1 else 'Não encontrado'
        ativo_imob_ultimo = list_ativos[1] if len(list_ativos) > 1 else 'Não encontrado'
              
        dict_company['AtivoImobAtual'] = ativo_imob_atualizado
        dict_company['AtivoImobUltimo'] = ativo_imob_ultimo
      
        
        # ATIVO TOTAL
        content, error = rgx.match([r'ativo total\s*(.*?)\n'], 1)
        
        ativo_total = error if error else content[0]
        list_ativos = ativo_total.split(' ')

        if len(list_ativos) == 1:
          ativo_total_atualizado, ativo_total_ultimo = split_string(ativo_total)
        else:
          ativo_total_atualizado = list_ativos[0]
          ativo_total_ultimo = list_ativos[1]
        
        dict_company['AtivoTotalAtual'] = ativo_total_atualizado
        dict_company['AtivoTotalUltimo'] = ativo_total_ultimo
           
        
        #TODO VER A LÓGICA DESSES 2 CAMPOS
        # PATRIMONIO LIQUIDO ATRIBUIDO A CONTROLADORA
        content, error = rgx.match([r'patrimonio liquido atribuido a controladora\s*(.*?)\n'], 1)
        list_patrim_liq_controladora = error if error else content[0]
        
        # PATRIMONIO LIQUIDO                   
        content, error = rgx.match([r"patrimonio liquido\s*(.*?)\n"], 1)
        patrim_liquido = error if error else content[0]
    
        
      if 'balanco patrimonial - consolidado' in text:
        # RECEITA DE VENDA
        content, error = rgx.match([r'receita de venda\s*(.*?)\n', r'venda\s*(.*?)\n'], 1)
        receita_venda = error if error else content[0]
        print(receita_venda)
        
        list_receita = receita_venda.split(' ')
        
        receita_venda_atualizado = list_receita[0] if len(list_receita) > 1 else 'Não encontrado'
        receita_venda_ultimo = list_receita[1] if len(list_receita) > 1 else 'Não encontrado'
                  
        if receita_venda_atualizado == 'Não encontrado':
          receita_venda_atualizado, receita_venda_ultimo = split_string(receita_venda)
          
  
        dict_company['ReceitaVendaAtual'] = receita_venda_atualizado
        dict_company['ReceitaVendaUltimo'] = receita_venda_ultimo
        