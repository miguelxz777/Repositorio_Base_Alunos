import json
#dados_json = '{"nome":"miguel", "idade":15, "cidade":"santana de parnaiba"}'
#dados_python = json.loads(dados_json)
#print(dados_python["nome"])
#print(dados_python["idade"])
pythonValue = {'cachorro': True,'raça':'salsicha/Rottweiler','nome':'mano','cor':'preto/laranja','genero':'macho','porte':'pequeno','bricadeira favorita':'rasgar a coberta','lugar preferido de dormir': 'sofa', 'idade':3,}
stringJsonData = json.dumps(pythonValue)
print(stringJsonData)