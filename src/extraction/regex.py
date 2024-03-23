import re


class Regex:
  """
  Classe para realizar operações de expressões regulares (REGEX) em um texto, 
  como encontrar padrões específicos, substituir padrões por novos valores, ou extrair informações específicas baseadas em padrões predefinidos.
  """
  def __init__(self, text: str):
    self.text = text
  
  
  def match(self, target: list[str], len_group: int):
    for t in target:
      pattern = re.compile(t, re.DOTALL)
      match = pattern.search(self.text)
      
      
      if match:
        return [match.group(i) for i in range(1, len_group + 1)], None
      
    return [], 'Não encontrado'
