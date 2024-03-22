from src.api.repositories.queries import *
from src.utils.functions.json_utils import JsonUtils
import locale


def fill_all_jsons_responses():
  """
  Função responsável por preencher todos os JSONs com as informações do .csv por meio de insights para popular as perguntas e respostas do ChatBot.
  """
  locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
  json_utils = JsonUtils()
  
  # Empresa_Mais_Acoes
  empresa, acoes = return_company_most_acoes()
  
  lists_empresa_mais_acoes_responses = [
    f"A empresa com mais ações é a {empresa} com {int(acoes)} ações.",
    f"A empresa que detêm mais ações é a {empresa} com {int(acoes)} ações."
  ]
  
  json_utils.fill_json("Empresa_Mais_Acoes", lists_empresa_mais_acoes_responses)
  
  # Empresa_Menos_Acoes
  empresa, acoes = return_company_least_acoes()
  
  list_empresa_menos_acoes_responses = [
    f"A empresa com menos ações é a {empresa} com {int(acoes)} ações.",
    f"A empresa que detêm menos ações é a {empresa} com {int(acoes)} ações."
  ]
  
  json_utils.fill_json("Empresa_Menos_Acoes", list_empresa_menos_acoes_responses)
  
  # Empresa_Mais_Investidores
  empresa, codigo, invests = return_most_invests_total()
  
  list_empresa_mais_investidores_responses = [
    f"A empresa com mais investidores é a {empresa} ({codigo}) com {int(invests)} investidores.",
    f"A empresa que detêm mais investidores é a {empresa} ({codigo}) com {int(invests)} investidores."
  ]
  
  json_utils.fill_json("Empresa_Mais_Investidores", list_empresa_mais_investidores_responses)
  
  # Empresa_Mais_Investidores_PFisica
  empresa, invests = return_company_most_invests_PFisica()
  
  list_empresa_mais_investidores_PFisica_responses = [
    f"A empresa com mais investidores (Pessoa Física) é a {empresa} com {int(invests)} investidores.",
    f"A empresa que detêm mais investidores (Pessoa Física) é a {empresa} com {int(invests)} investidores."
  ]
  
  json_utils.fill_json("Empresa_Mais_Investidores_PFisica", list_empresa_mais_investidores_PFisica_responses)
  
  
  # Empresa_Mais_Investidores_PJuridica
  empresa, invests = return_company_most_invests_PJuridica()
  
  list_empresa_mais_investidores_PJuridica_responses = [
    f"A empresa com mais investidores (Pessoa Jurídica) é a {empresa} com {int(invests)} investidores.",
    f"A empresa que detêm mais investidores (Pessoa Jurídica) é a {empresa} com {int(invests)} investidores."
  ]
  
  json_utils.fill_json("Empresa_Mais_Investidores_PJuridica", list_empresa_mais_investidores_PJuridica_responses)
  
  
  # Empresa_Mais_Investidores_Institucionais
  empresa, invests = return_company_most_invests_Insti()
  
  list_empresa_mais_investidores_Institucionais_responses = [
    f"A empresa com mais investidores institucionais é a {empresa} com {int(invests)} investidores.",
    f"A empresa que detêm mais investidores institucionais é a {empresa} com {int(invests)} investidores."
  ]
  
  json_utils.fill_json("Empresa_Mais_Investidores_Institucionais", list_empresa_mais_investidores_Institucionais_responses)
  
  
  # Empresa_Mais_Capital_Social
  empresa, capital = return_company_most_capital_social()
  
  capital = locale.currency(capital, grouping=True)
  
  list_empresa_mais_capital_social_responses = [
    f"A empresa com mais capital social é a {empresa} com {capital}",
    f"A empresa que detêm mais capital social é a {empresa} com {capital}"
  ]
  
  json_utils.fill_json("Empresa_Mais_Capital_Social", list_empresa_mais_capital_social_responses)
  
  
  # Empresa_Mais_Patrimonio_Liquido
  empresa, patrimonio = return_company_most_patrimonio_liquido()
  
  list_empresa_mais_patrimonio_liquido_responses = [
    f"A empresa com mais patrimônio líquido é a {empresa} com {locale.currency(patrimonio, grouping=True)}",
    f"A corretora que detêm o maior patrimônio líquido é a {empresa} com {locale.currency(patrimonio, grouping=True)}"
  ]
  
  json_utils.fill_json("Empresa_Mais_Patrimonio_Liquido", list_empresa_mais_patrimonio_liquido_responses)
  
    
  # Todas_Empresas
  list_companies = return_all_companies()
  
  str_companies = '\nAqui está a lista de todas as empresas no Banco de Dados\n'
  for companie in list_companies:
    str_companies += f"\n- {companie}"
    
  json_utils.fill_json("Todas_Empresas", [str_companies])

  
  # TOP3_Empresa_Maior_Evolucao_Resultado_Bruto
  list_empresa, codigo, list_evolucao = return_top3_most_evolucao_resultado_bruto()
  
  str_top3 = '\nAqui Estão 3 empresas com os melhores números de crescimento do Resultado Bruto\n'
  for i in range(3):
    str_top3 += (
      f"\n{i+1}º - A empresa {list_empresa[i]} ({codigo[i]}) teve um crescimento de {locale.currency(list_evolucao[i], grouping=True)} no resultado bruto."
    )
  
  json_utils.fill_json("TOP3_Empresa_Maior_Evolucao_Resultado_Bruto", [str_top3])
  
  
  # TOP5_Empresa_Maior_Evolucao_Patrimonio_Liquido
  list_empresa, codigo, list_evolucao = return_top5_most_evolucao_patrim_liq()

  str_top5 = '\nAqui Estão 5 empresas com os melhores números de crescimento do Patrimônio Líquido\n'
  for i in range(5):
    str_top5 += (
      f"\n{i+1}º - A empresa {list_empresa[i]} ({codigo[i]}) teve um crescimento de {locale.currency(list_evolucao[i], grouping=True)} no patrimônio líquido."
    )
  
  json_utils.fill_json("TOP5_Empresa_Maior_Evolucao_Patrimonio_Liquido", [str_top5])
  
  
  # CRIAR JSON COM TODAS AS EMPRESAS E SUAS INFORMAÇÕES
  list_companies = return_all_companies_infos()
  for company in list_companies:
    dict_infos = dict()
    
    dict_infos['patterns'] = [f"Qual a situação da empresa {company[1]}?", f"Como está a empresa {company[1]}?", f"Me fale sobre a empresa {company[1]}", f"Fale da {company[1]}",
    f"Qual a situação da empresa {company[1]}", f"Como está a empresa {company[1].lower()}", f"Me fale sobre a empresa {company[1].lower()}",f"Fale da {company[1].lower()}",
    f"Qual a descrição do Ativo {company[1]}", f"Como está o ativo {company[1]}", f"Me fale sobre o ativo {company[1]}", f"Fale do ativo {company[1]}",
    f"Qual a descrição do Ativo {company[1].lower()}", f"Como está o ativo {company[1].lower()}"]
    
    
    dict_infos['responses'] = [f"""\nAqui estão as informações sobre a empresa atualizado na data: {company[0]}
                               \n{company[1]} ({company[2]}):
                               \n\t- CNPJ: {company[3]}
                               \n\t- Site: {company[5]}
                               \n\t- Ativo Imobilizado, Investimentos e intangível: {locale.currency(company[8], grouping=True)} (Atual)
                               \n\t- Ativo Imobilizado, Investimentos e intangível: {locale.currency(company[9], grouping=True)} (Anterior)
                               \n\t- Ativo Total: {locale.currency(company[10], grouping=True)} (Atual)
                               \n\t- Ativo Total: {locale.currency(company[11], grouping=True)} (Anterior)
                               \n\t- Lucro(Prejuízo) do Período: {locale.currency(company[20], grouping=True)} (Atual)
                               \n\t- Lucro(Prejuízo) do Período: {locale.currency(company[21], grouping=True)} (Anterior)
                               \n\t- Total Ações: {int(company[36])}
                               \n\t- Total Investidores: {int(company[41])}
                               \n\t- Patrimônio Líquido: {locale.currency(company[12], grouping=True)}
                               \n\t- Composição do Capital: {locale.currency(company[40], grouping=True)}
                               """]    
    
    json_utils.append_json(dict_infos, company[1])