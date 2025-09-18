def for1():
    L =[1,2,3,4,5,6,7,8,9,10]
    for miguel in L:
        print(miguel)
#for1()

def for2():
    carros=["fusca","civic","jetta","gol","saveiro"]
    for s in carros:
        for letra in carros:
            print(letra)
#for2()

def for3():
    L=[1,5,8,3,9,4,6,2,7,9]
    maximo=L[0]
    for e in L:
        if e > maximo:
            maximo = e
    print(maximo)
#for3()

def exibir_minimo():
    L=[9,5,8,2,3,4,5]
    minimo=L[0]
    for e in L:
        if e < minimo:
            minimo = e
            print(minimo)
#exibir_minimo()

def range1():
    for v in range(5,8):
        print(v)
#range1()

def virgula():
    for t in range(3,33,3):
      print(t,end="")
#virgula()

def composição_string():
    nome = "miguel"
    idade = 22
    grana = 51.34
    print("%20s tem %010d anos e RS%5.2f no bolso." % (nome,idade,grana))
#composição_string()
