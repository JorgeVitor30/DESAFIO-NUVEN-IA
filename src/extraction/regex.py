import re


class Regex:
  def __init__(self, text: str):
    self.text = text
  
  
  def match(self, target: list[str], len_group: int):
    for t in target:
      pattern = re.compile(t, re.DOTALL)
      match = pattern.search(self.text)
      
      
      if match:
        return [match.group(i) for i in range(1, len_group + 1)], None
      
    return [], 'Não encontrado'
  
  

