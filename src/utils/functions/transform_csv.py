import pandas as pd
import numpy as np
import os


def transform_csv(dict_infos: dict) -> pd.DataFrame:
  nome_arquivo = 'output.csv'
  
  if os.path.isfile(nome_arquivo):
    df = pd.read_csv(nome_arquivo, sep=';', encoding='utf-8')
    
  else:
    columns = ['DataAttPDF', 'NomePregao', 'CodNegociacao', 'CNPJ', 'CassifSetor', 'Site', 'DatAtualAtlz', 'DatUltimAtlz', 'AtivoImobAtual', 'AtivoImobUltimo', 'AtivoTotalAtual', 'AtivoTotalUltimo', 'PatrimLiquidoAtual', 'PatrimLiquidoUltimo', 'PatrimLiqControladoraAtual', 'PatrimLiqControladoraUltimo', 'ReceitaVendaAtual', 'ReceitaVendaUltimo', 'ResultadoBrutoAtual', 'ResultadoBrutoUltimo', 'LucroPrejPeriodoAtual', 'LucroPrejPeriodoUltimo', 'ResultEquivalenciaAtual', 'ResultEquivalenciaUltimo', 'ResultFinanceiroAtual', 'ResultFinanceiroUltimo', 'AtividOperacionaisAtual', 'AtividOperacionaisUltimo', 'AtividInvestAtual', 'AtividInvestUltimo', 'AtividFinancAtual', 'AtividFinancUltimo', 'VariacaoCambialAtual', 'VariacaoCambialUltimo', 'AumentoCaixaAtual', 'AumentoCaixaUltimo', 'TotalAcoes' ,'InvestPFisicas', 'InvestPJuridicas', 'InvestInstitucionais', 'ComposicaoCapital', 'TotalInvests', 'VariacaoPatrimLiquido', 'VariacaoReceitaVenda', 'VariacaoLucroPrejPeriodo', 'VariacaoResultadoBruto', 'VariacaoAtividOperacionais', 'VariacaoAtividInvest', 'VariacaoAtividFinanc']
    
    df = pd.DataFrame(columns=columns)
  
  df.loc[len(df)] = dict_infos
  
  df.to_csv(nome_arquivo, index=False, sep=';', encoding='utf-8')
