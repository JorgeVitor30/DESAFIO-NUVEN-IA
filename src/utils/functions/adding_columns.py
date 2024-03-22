import pandas as pd


def adding_columns(df: pd.DataFrame):
  """
  Função para adicionar colunas ao DataFrame em base de outras colunas.
  """
  # Coluna TotalInvests
  df['TotalInvests'] = int(df['InvestPFisicas'] + df['InvestPJuridicas'] + df['InvestInstitucionais'])
  
  # Coluna Delta PatrimLiquido
  df['VariacaoPatrimLiquido'] = df['PatrimLiquidoAtual'] - df['PatrimLiquidoUltimo']
  
  # Coluna Delta ReceitaVenda
  df['VariacaoReceitaVenda'] = df['ReceitaVendaAtual'] - df['ReceitaVendaUltimo']
  
  # Coluna Delta LucroPrejPeriodo
  df['VariacaoLucroPrejPeriodo'] = df['LucroPrejPeriodoAtual'] - df['LucroPrejPeriodoUltimo']
  
  # Coluna Delta ResultadoBrutoAtual
  df['VariacaoResultadoBruto'] = df['ResultadoBrutoAtual'] - df['ResultadoBrutoUltimo']
  
  # Coluna Delta AtividOperacionais
  df['VariacaoAtividOperacionais'] = df['AtividOperacionaisAtual'] - df['AtividOperacionaisUltimo']
  
  # Coluna Delta AtividInvest
  df['VariacaoAtividInvest'] = df['AtividInvestAtual'] - df['AtividInvestUltimo']
  
  # Coluna Delta AtividFinanc
  df['VariacaoAtividFinanc'] = df['AtividFinancAtual'] - df['AtividFinancUltimo']
  