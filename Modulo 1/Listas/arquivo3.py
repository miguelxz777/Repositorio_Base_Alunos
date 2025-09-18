import os 
try:
    for n in range(1,51):
        os.mkdir("pasta_%d" % n)
        os.chdir("pasta_%d" % n)
        arquivo = open("arquivo.txt"<"w")
        arquivo.write("oi")
        arquivo.close()
        os.chdir("..")
except FileNotFoundError:
    print('arquivo nao encontrado')
