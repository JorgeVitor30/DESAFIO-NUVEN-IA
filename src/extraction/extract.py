import re
import datetime
import pandas

from PyPDF2 import PdfReader
from src.extraction.regex import Regex
from src.utils.functions.split_big_string import split_string, split_string2, split_string3
from src.utils.functions.remove_accent import remove_accent


class Extract:
  """
  Classe para a extração de PDF
  -> Retorna um dicionário com as informações relevantes vindas do PDF.
  """
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
          ativo_total_atualizado, ativo_total_ultimo = split_string3(ativo_total)
        else:
          ativo_total_atualizado = list_ativos[0]
          ativo_total_ultimo = list_ativos[1]
        
        dict_company['AtivoTotalAtual'] = ativo_total_atualizado
        dict_company['AtivoTotalUltimo'] = ativo_total_ultimo
           
        
        # PATRIMONIO LIQUIDO                   
        content, error = rgx.match([r"patrimonio liquido\s*(.*?)\n"], 1)
        patrim_liquido = error if error else content[0]
        
        if ')(' in patrim_liquido:
          list_patrim_liquido = patrim_liquido.split(')(')
          patrim_liquido_atual, patrim_liquido_ultimo = list_patrim_liquido[0], list_patrim_liquido[1]
        else:
          list_liquido = patrim_liquido.split(' ') 
           
          if len(list_liquido) == 1:
            patrim_liquido_atual, patrim_liquido_ultimo = split_string(patrim_liquido)
          else:
            patrim_liquido_atual = list_liquido[0]
            patrim_liquido_ultimo = list_liquido[1]
          
        dict_company['PatrimLiquidoAtual'] = patrim_liquido_atual
        dict_company['PatrimLiquidoUltimo'] = patrim_liquido_ultimo
        
        
        # PATRIMONIO LIQUIDO ATRIBUIDO A CONTROLADORA
        content, error = rgx.match([r'patrimonio liquido atribuido a controladora\s*(.*?)\n'], 1)
        patrim_liq_controladora = error if error else content[0]
        
        if ')(' in patrim_liq_controladora:
          list_patrim_liq_controladora = patrim_liq_controladora.split(')(')
          patrim_liq_controladora_atual, patrim_liq_controladora_ultimo = list_patrim_liq_controladora[0], list_patrim_liq_controladora[1]
        else:
          list_liq_controladora = patrim_liq_controladora.split(' ')
          if len(list_liq_controladora) == 1:
            patrim_liq_controladora_atual, patrim_liq_controladora_ultimo = split_string(patrim_liq_controladora)
          else:
            patrim_liq_controladora_atual = list_liq_controladora[0]
            patrim_liq_controladora_ultimo = list_liq_controladora[1]
        
        dict_company['PatrimLiqControladoraAtual'] = patrim_liq_controladora_atual
        dict_company['PatrimLiqControladoraUltimo'] = patrim_liq_controladora_ultimo
      
        
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
    
    
      if 'atividades operacionais' in text:
        # ATIVIDADES OPERACIONAIS
        content, error = rgx.match([r'atividades operacionais\s*(.*?)\n'], 1)
        ativ_operacionais = error if error else content[0]
        
        list_ativ_operacionais = ativ_operacionais.split(' ')
        
        ativid_operacionais_atualizado = list_ativ_operacionais[0] if len(list_ativ_operacionais) >= 1 else 'Não encontrado'
        ativid_operacionais_ultimo = list_ativ_operacionais[1] if len(list_ativ_operacionais) > 1 else 'Não encontrado'
      
        dict_company['AtividOperacionaisAtual'] = ativid_operacionais_atualizado
        dict_company['AtividOperacionaisUltimo'] = ativid_operacionais_ultimo
    
    
      if 'atividades de investimento' in text:
        # ATIVIDADES DE INVESTIMENTO ATUALIZADO
        content, error = rgx.match([r'atividades de investimento\s*(.*?)\s'
                                    ], 1)
        ativ_invest = error if error else content[0]
        
        list_ativ_invest = ativ_invest.split(' ')
        
        if ')(' in ativ_invest:
          ativ_invest_atualizado = ativ_invest.split(')(')[0]
        else:
          ativ_invest_atualizado = list_ativ_invest[0] if len(list_ativ_invest) >= 1 else 'Não encontrado'
        
        dict_company['AtividInvestAtual'] = ativ_invest_atualizado
        
        # ATIVIDADES DE INVESTIMENTO ULTIMO
        content, error = rgx.match([r'atividades de investimento\s*(.*?)\n',
                                    r'atividades de investimento\s*(.*?)\s',
                                    r'atividades de investimento\s*(.*?)\s mais',
                                    r'atividades de investimento\s*(.*?)\n mais',
                                    r'atividades de investimento\s*(.*?)\s mais noticias'], 1)
        ativ_invest_ult = error if error else content[0]
        
        list_ativs_invest_ult = ativ_invest_ult.replace('mais', '').split(' ')
        
        if len(list_ativs_invest_ult) == 1:
          ativ_invest_ultimo = '0'
        else:
          ativ_invest_ultimo = list_ativs_invest_ult[1]
        
        dict_company['AtividInvestUltimo'] = ativ_invest_ultimo
          
      
      if 'atividades de financiamento' in text:
        # ATIVIDADES DE FINANCIAMENTO
        content, error = rgx.match([r'atividades de financiamento\s*(.*?)\n', r'de financiamento\s*(.*?)\n', r'financiamento\s*(.*?)\n'], 1)
        ativ_financ = error if error else content[0]
        
        if ')(' in ativ_financ:
          list_ativ_financ = ativ_financ.split(')(')
          ativid_financ_atualizado = list_ativ_financ[0]
          ativid_financ_ultimo = list_ativ_financ[1]
        else:
          list_ativ_financ = ativ_financ.split(' ')
          ativid_financ_atualizado = list_ativ_financ[0]
          ativid_financ_ultimo = list_ativ_financ[1]
          
        dict_company['AtividFinancAtual'] = ativid_financ_atualizado
        dict_company['AtividFinancUltimo'] = ativid_financ_ultimo
      
      
      if 'variacao cambial sobre caixa' in text:
        # VARIAÇÃO CAMBIAL SOBRE CAIXA
        content, error = rgx.match([r'variacao cambial sobre caixa e equivalentes\s*(.*?)\n'], 1)
        variacao_cambial = error if error else content[0]
        
        list_variacao_cambial = variacao_cambial.replace(')(', ' ').split(' ')
        
        variacao_cambial_atualizado = list_variacao_cambial[0] if len(list_variacao_cambial) >= 1 else 'Não encontrado'
        variacao_cambial_ultimo = list_variacao_cambial[1] if len(list_variacao_cambial) > 1 else 'Não encontrado'
        
        dict_company['VariacaoCambialAtual'] = variacao_cambial_atualizado
        dict_company['VariacaoCambialUltimo'] = variacao_cambial_ultimo
      
      
      if 'aumento (reducao) de caixa e equivalentes' in text:
        # AUMENTO(REDUÇÃO) DE CAIXA E EQUIVALENTES
        text_ = text.replace(')', '').replace('(', '')
        rgx2 = Regex(text_)
        content, error = rgx2.match([r'aumento reducao de caixa e equivalentes\s*(.*?)\n', r'de caixa e equivalentes\s*(.*?)\n'], 1)
        aumento_caixa = error if error else content[0]
        
        list_aumento_caixa = aumento_caixa.split(' ')
        if len(list_aumento_caixa) == 1:
          aumento_caixa_atualizado, aumento_caixa_ultimo = split_string2(aumento_caixa)
        else:
          aumento_caixa_atualizado = list_aumento_caixa[0]
          aumento_caixa_ultimo = list_aumento_caixa[1]
       
        dict_company['AumentoCaixaAtual'] = aumento_caixa_atualizado
        dict_company['AumentoCaixaUltimo'] = aumento_caixa_ultimo
      
               
      if 'pessoas fisicas' in text and 'pessoas juridicas':
        # PESSOAS FISICAS
        content, error = rgx.match([r'pessoas fisicas\s*(.*?)-'], 1)
        investidores_fisicas = error if error else content[0].strip()
        
        dict_company['InvestPFisicas'] = investidores_fisicas
  
  
        # PESSOAS JURIDICAS
        content, error = rgx.match([r'pessoas juridicas\s*(.*?)-'], 1)
        investidores_juridicas = error if error else content[0].strip()
         
        dict_company['InvestPJuridicas'] = investidores_juridicas
        
        
        # INVESTIDORES INSTITUCIONAIS
        content, error = rgx.match([r'investidores institucionais\s*(.*?)-'], 1)
        investidores_insti = error if error else content[0].strip()

        dict_company['InvestInstitucionais'] = investidores_insti  
    
    
      if 'acoes' in text:
        # TOTAL DE AÇÕES
        content, error = rgx.match([r'total de acoes\s*(.*?)\s'], 1)
        total_acoes = error if error else content[0]

        dict_company['TotalAcoes'] = total_acoes
      
      if i == (self.pages - 1):
        # COMPOSIÇÃO DO CAPITAL SOCIAL
        text_ = text[text.find('preferencia'):]
        rgx2 = Regex(text_)
    
        content, error = rgx2.match([r'total\s*(.*?)\s'], 1)
        composicao_capital = error if error else content[0]
        
        composicao_capital = text_[-14: ].replace('al', '').replace('l', '').replace('tal', '').strip()
      
        dict_company['ComposicaoCapital'] = composicao_capital

    return dict_company
      