try:
    arquivo=open("numeros.txt","w")
    for linha in range(1,50000):
        arquivo.write("%dmiguel\n" % linha)
    arquivo.close()
except FileNotFoundError:
    print('arquivo nao encontrado')