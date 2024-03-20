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
                 
        
      if 'balanco patrimonial' in text:
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
        
        list_receita = receita_venda.split(' ')
        
        receita_venda_atualizado = list_receita[0] if len(list_receita) > 1 else 'Não encontrado'
        receita_venda_ultimo = list_receita[1] if len(list_receita) > 1 else 'Não encontrado'
                  
        if receita_venda_atualizado == 'Não encontrado':
          receita_venda_atualizado, receita_venda_ultimo = split_string(receita_venda)
          
        dict_company['ReceitaVendaAtual'] = receita_venda_atualizado
        dict_company['ReceitaVendaUltimo'] = receita_venda_ultimo
      
      
        # RESULTADO BRUTO
        content, error = rgx.match([r'resultado bruto\s*(.*?)\n'], 1)
        resultado_bruto = error if error else content[0]
        if 'financeira' in resultado_bruto:
          resultado_bruto = resultado_bruto[resultado_bruto.find('financeira') + 10:].strip()
          
        list_resultado = resultado_bruto.split(' ')
        
        resultado_bruto_atualizado = list_resultado[0] if len(list_resultado) > 1 else 'Não encontrado'
        resultado_bruto_ultimo = list_resultado[1] if len(list_resultado) > 1 else 'Não encontrado'
  
        dict_company['ResultadoBrutoAtual'] = resultado_bruto_atualizado
        dict_company['ResultadoBrutoUltimo'] = resultado_bruto_ultimo
        
        
        # LUCRO (PREJUIZO) DO PERIODO
        content, error = rgx.match([r'lucro \(prejuizo\) do periodo\s*(.*?)\n'], 1)
        lucro_periodo = error if error else content[0]
        list_lucro = lucro_periodo.split(' ')
        
        lucro_periodo_atualizado = list_lucro[0] if len(list_lucro) > 1 else 'Não encontrado'
        lucro_periodo_ultimo = list_lucro[1] if len(list_lucro) > 1 else 'Não encontrado'
        
        dict_company['LucroPrejPeriodoAtual'] = lucro_periodo_atualizado
        dict_company['LucroPrejPeriodoUltimo'] = lucro_periodo_ultimo
        
      if 'resultado de equivalencia patrimonial' in text:
        # RESULTADO DE EQUIVALÊNCIA PATRIMONIAL
        content, error = rgx.match([r'resultado de equivalencia patrimonial\s*(.*?)\n'], 1)
        result_equivalencia = error if error else content[0]
        
        list_result_equivalencia = result_equivalencia.split(' ')
        
        if len(list_result_equivalencia) == 1:
          result_equivalencia_atualizado, result_equivalencia_ultimo = list_result_equivalencia[0].split(')(')
        else:
          result_equivalencia_atualizado = list_result_equivalencia[0] if len(list_result_equivalencia) >= 1 else 'Não encontrado'
          result_equivalencia_ultimo = list_result_equivalencia[1] if len(list_result_equivalencia) > 1 else 'Não encontrado'
        
        dict_company['ResultEquivalenciaAtual'] = result_equivalencia_atualizado
        dict_company['ResultEquivalenciaUltimo'] = result_equivalencia_ultimo
      
      
      if 'demonstracao do resultado' in text:
        # RESULTADO FINANCEIRO
        content, error = rgx.match([r'resultado financeiro\s*(.*?)\n'], 1)
        result_financeiro = error if error else content[0]
        
        list_result_financeiro = result_financeiro.split(' ')
        
        if len(list_result_financeiro) == 1:
          result_financeiro_atualizado, result_financeiro_ultimo = list_result_financeiro[0].split(')(')
        else:
          result_financeiro_atualizado = list_result_financeiro[0] if len(list_result_financeiro) >= 1 else 'Não encontrado'
          result_financeiro_ultimo = list_result_financeiro[1] if len(list_result_financeiro) > 1 else 'Não encontrado'
        
        dict_company['ResultFinanceiroAtual'] = result_financeiro_atualizado
        dict_company['ResultFinanceiroUltimo'] = result_financeiro_ultimo
