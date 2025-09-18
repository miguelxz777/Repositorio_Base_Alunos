import types
def diz_o_tipo(a):
  tipo = type(a)
  if tipo == str:
    return("String")
  elif tipo == list:
    return("Lista")
  elif tipo == dict:
    return("Dicionário")
  elif tipo == int:
    return("Número inteiro")
  elif tipo == float:
    return("Número decimal")
  elif tipo == types.FunctionType:
    return("Função")
  elif tipo == types.BuiltinFunctionType:
    return("Função interna")
  else:
    return(str(tipo))

def minha_funcao(x,y):
    return x+y
    print(f"tipo de(1,2):{diz_o_tipo((1,2))}")
print(f"tipo de 'ola': {diz_o_tipo([1,2,3])}")
print(f"tipo de {{'a' : 1}}: {diz_o_tipo({'a':1})}")
print(f"tipo de 10: {diz_o_tipo(10)}")
print(f"tipo de 3,14: {diz_o_tipo(3.14)}")
print(f"tipo de(minha_funcao)")
print(f"diz_o_tipo de(len)")
print(f"tipo de(1,2):{diz_o_tipo((1,2))}")