def pronto(): 
  pass

def cumprimentar_a(quien, horario):
  if horario < 12:
    return "Bom dia " + quien
  elif horario < 19:
    return "Boa tarde " + quien
  else: 
    return "Boa noite " + quien
    
def cumprimentar_a_recarregado(quien, horario):
  if horario < 19:
    return "Boa tarde " + quien
  elif horario < 12:
    return "Bom dia " + quien
  else: 
    return "Boa noite " + quien
    