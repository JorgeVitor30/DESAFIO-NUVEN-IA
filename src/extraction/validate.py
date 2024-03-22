class Validate:
  """
  Classe responsável por validar os dados extraídos do PDF.
  Validações como: remover pontos, remover parenteses de números, tratar valores não informados e transformar strings em float e int estão nessa classe.
  """
  def __init__(self, dict_pdf: dict):
    self.dict = dict_pdf
  
  
  def all_validations(self):
    self.remove_num_points()
    self.remove_number_parents()
    self.treat_uninformed_values()
    self.transform_str_to_float_and_int()
    
    return self.dict
  
  
  def remove_num_points(self):    
    for key in self.dict.keys():
      # Verificação pra campos não numéricos
      if (key == 'DataAttPDF') or (key == 'NomePregao') or (key == 'CodNegociacao') or (key == 'CNPJ') or (key == 'CassifSetor') or (key == 'DatAtualAtlz') or (key == 'DatUltimAtlz') or (key == 'Site'):
        continue
      
      self.dict[key] = self.dict[key].replace('.', '')
      
  
  def remove_number_parents(self):
    for key in self.dict.keys():
      # Verificação pra campos não numéricos
      if (key == 'DataAttPDF') or (key == 'NomePregao') or (key == 'CodNegociacao') or (key == 'CNPJ') or (key == 'CassifSetor') or (key == 'DatAtualAtlz') or (key == 'DatUltimAtlz') or (key == 'Site'):
        continue
      
      self.dict[key] = self.dict[key].replace('(', '')
      self.dict[key] = self.dict[key].replace(')', '')
    
  
  
  def treat_uninformed_values(self):
    for key in self.dict.keys():
      # Verificação pra campos não numéricos
      if (key == 'DataAttPDF') or (key == 'NomePregao') or (key == 'CodNegociacao') or (key == 'CNPJ') or (key == 'CassifSetor') or (key == 'DatAtualAtlz') or (key == 'DatUltimAtlz') or (key == 'Site'):
        continue
      
      if self.dict[key] == 'Não informado':
        self.dict[key] = 0
    
    
  def transform_str_to_float_and_int(self):
    for key in self.dict.keys():
      # Verificação pra campos não numéricos
      if (key == 'DataAttPDF') or (key == 'NomePregao') or (key == 'CodNegociacao') or (key == 'CNPJ') or (key == 'CassifSetor') or (key == 'DatAtualAtlz') or (key == 'DatUltimAtlz') or (key == 'Site'):
        continue
      
      if (key == 'TotalInvests') or (key == 'TotalAcoes') or (key == 'InvestPFisicas') or (key == 'InvestPJuridicas') or (key == 'InvestInstitucionais'):
        try:
          self.dict[key] = int(self.dict[key])
        except ValueError:
          self.dict[key] = 0
        continue
     
      try:
        self.dict[key] = float(self.dict[key])
      except ValueError:
        self.dict[key] = 0
      