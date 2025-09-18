def while_com_lista():
    L=[]
    while True:
        n = input("digite uma palavra ( ) sai ):")
        if n == "0":
            break
        L.append(n)
x=0
while x < len(L):
    print(L[x])
    x = x + 1
    print("L")
while_com_lista()