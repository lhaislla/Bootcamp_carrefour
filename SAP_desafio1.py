nota = int(input())
def converte(nota):
  resultado = ''
  while nota != '':
    if nota <= 0:
        resultado = 'E'
        return(resultado)
    elif 1 <= nota  and nota <= 35:
        resultado = 'D'
        return(resultado)
    elif  36 <= nota and nota <= 60:
      resultado = 'C'
      return(resultado)
    elif 61 <= nota and nota <= 85:
       resultado = 'B'
       return(resultado)
    elif 86 <= nota and nota <= 100:
        resultado = 'A'
        return(resultado)
    return(resultado)
print(converte(nota))
