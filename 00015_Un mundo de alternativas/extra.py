def pronto(): 
  pass

def cumprimentar_a(quien, horario):
  if horario < 12:
    return "Buenos días " + quien
  elif horario < 19:
    return "Buenas tardes " + quien
  else: 
    return "Buenas noches " + quien
    
def cumprimentar_a_recarregado(quien, horario):
  if horario < 19:
    return "Buenas tardes " + quien
  elif horario < 12:
    return "Buenos días " + quien
  else: 
    return "Buenas noches " + quien
    