def tabuada():
    n = int(input("tabuada de:"))
    fim = int(input("digitiate o fim:"))
    x = 1
    while x <= fim:
        print(n, "x", "=", n*x)
        x=x+1
#tabuada()
def while00():
    s=0
    while True:
        v=int(input("digite um numero a somar ou 0 para sair:"))
        if v==0:
            break
        s = s+v
    print(s)
while00()