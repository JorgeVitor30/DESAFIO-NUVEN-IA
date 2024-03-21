import pandas as pd
import numpy as np


# RETORNAR TODAS A QUANTIDADE DE TODAS AÇÕES DOS PDFs
def return_count_all_acoes():
  csv = pd.read_csv('output.csv', sep=';')
  
  return csv['TotalAcoes'].sum()


# RETORNAR A EMPRESA COM MAIS AÇÕES
def return_company_most_acoes():
  csv = pd.read_csv('output.csv', sep=';')
  
  max_total_acoes = csv['TotalAcoes'].max()
  
  row = csv[csv['TotalAcoes'] == max_total_acoes]
  
  return row['NomePregao'].values[0], row['TotalAcoes'].values[0] 
  

# RETORNAR A EMPRESA COM MENOS AÇÕES
def return_company_least_acoes():
  csv = pd.read_csv('output.csv', sep=';')
  
  min_total_acoes = csv['TotalAcoes'].min()
  
  row = csv[csv['TotalAcoes'] == min_total_acoes]
  
  return row['NomePregao'].values[0], row['TotalAcoes'].values[0]


# RETORNAR A EMPRESA COM MAIS INVESTIDORES (PESSOAS FISICAS)
def return_company_most_invests_PFisica():
  csv = pd.read_csv('output.csv', sep=';')
  
  max_invests_people = csv['InvestPFisicas'].max()
  
  row = csv[csv['InvestPFisicas'] == max_invests_people]
  
  return row['NomePregao'].values[0], row['InvestPFisicas'].values[0]


# RETORNAR A EMPRESA COM MAIS INVESTIDORES (PESSOAS JURIDICAS)
def return_company_most_invests_PJuridica():
  csv = pd.read_csv('output.csv', sep=';')
  
  max_invest_people = csv['InvestPJuridicas'].max()
  
  return csv[csv['InvestPJuridicas'] == max_invest_people]['NomePregao'].values[0], max_invest_people


# RETORNAR A EMPRESA COM MAIS INVESTIDORES INSTITUCIONAIS
def return_company_most_invests_Insti():
  csv = pd.read_csv('output.csv', sep=';')
  
  max_invest_people = csv['InvestInstitucionais'].max()
  
  return csv[csv['InvestInstitucionais'] == max_invest_people]['NomePregao'].values[0], max_invest_people


# RETORNAR A EMPRESA COM MAIS INVESITDORES NO TOTAL
def return_most_invests_total():
  csv = pd.read_csv('output.csv', sep=';')
  
  max_invest_people = csv['TotalInvests'].max()
  
  
  return csv[csv['TotalInvests'] == max_invest_people]['NomePregao'].values[0], csv[csv['TotalInvests'] == max_invest_people]['CodNegociacao'].values[0], max_invest_people


# RETORNAR 3 EMPRESAS COM MAIORES EVOLUÇÕES DO RESULTADO BRUTO
def return_top3_most_evolucao_resultado_bruto():
  csv = pd.read_csv('output.csv', sep=';')
  
  filtered_df = csv[(csv['ResultadoBrutoAtual'] != 0) & (csv['ResultadoBrutoUltimo'] != 0)]

  sorted_df = filtered_df.sort_values(by='VariacaoResultadoBruto', ascending=False)
  
  top3_empresas = sorted_df.head(3)
  
  return top3_empresas['NomePregao'].values.tolist(), top3_empresas['CodNegociacao'].values.tolist(), top3_empresas['VariacaoResultadoBruto'].values.tolist()


# RETORNAR EMPRESA COM MAIOR EVOLUÇÃO DO PATRIMONIO LIQUIDO
def return_most_evolucao_patrim_liq():
  csv = pd.read_csv('output.csv', sep=';')
  
  filtered_df = csv[(csv['PatrimLiquidoUltimo'] != 0) & (csv['PatrimLiquidoUltimo'] != 0)]
  
  max_evolucao_patrim_liquido = filtered_df['VariacaoPatrimLiquido'].max()
  
  return csv[csv['VariacaoPatrimLiquido'] == max_evolucao_patrim_liquido]['NomePregao'].values[0], max_evolucao_patrim_liquido


# RETORNAR TODOS OS NOMES DA EMPRESA
def return_all_companies():
  csv = pd.read_csv('output.csv', sep=';')
  
  return csv['NomePregao'].values.tolist()


# RETORNAR EMPRESA COM MAIOR CAPITAL SOCIAL
def return_company_most_capital_social():
  csv = pd.read_csv('output.csv', sep=';')
  
  max_capital_social = csv['ComposicaoCapital'].max()
  
  return csv[csv['ComposicaoCapital'] == max_capital_social]['NomePregao'].values[0], max_capital_social 


# RETORNAR EMPRESA COM MAIOR PATRIMONIO LIQUIDO
def return_company_most_patrimonio_liquido():
  csv = pd.read_csv('output.csv', sep=';')
  
  max_patrim_liquido = csv['PatrimLiquidoAtual'].max()
  
  return csv[csv['PatrimLiquidoAtual'] == max_patrim_liquido]['NomePregao'].values[0], max_patrim_liquido


# RETORNAR TOP 5 EMPRESAS COM MAIOR CRESCIMENTO DE PATRIMONIO LIQUIDO
def return_top5_most_evolucao_patrim_liq():
  csv = pd.read_csv('output.csv', sep=';')
  
  sorted_df = csv.sort_values(by='VariacaoPatrimLiquido', ascending=False)

  top5_empresas = sorted_df.head(5)
  
  return top5_empresas['NomePregao'].values.tolist(), top5_empresas['CodNegociacao'].values.tolist(), top5_empresas['VariacaoPatrimLiquido'].values.tolist()


# RETORNAR TODAS AS EMPRESAS COM TODAS AS INFOS
def return_all_companies_infos():
  csv = pd.read_csv('output.csv', sep=';')
  
  return csv.values.tolist()
