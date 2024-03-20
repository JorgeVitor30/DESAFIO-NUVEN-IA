
def split_string(num_string):

  terceiro_ponto_index = num_string.find(".", num_string.find(".", num_string.find(".") + 1) + 1)

  str1 = num_string[:terceiro_ponto_index -3]
  str2 = num_string[terceiro_ponto_index -3:]

  return str1, str2