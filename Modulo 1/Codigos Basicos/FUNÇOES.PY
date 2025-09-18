"""texto_escrito="este livro é legal!"
outro_texto='vou aprender programar.'
texto="""
#primeira linha
#segunda linha
#terceira linha
"""
print("\tOi!\neu me chamo \"(miguel jose)\"!!!")
outro_texto = texto_escrito
print(outro_texto)
peçasdebike_subtraidas = 15
quantidades_peçasdebike = 25
quantidades_peçasdebike -= peçasdebike_subtraidas
print(quantidades_peçasdebike)
quantidades_peçasdebike += 300
print(quantidades_peçasdebike)
quantidades_peçasdebike -= 23
carteira_digital=0
print(carteira_digital)
carteira_digital +=100
print(carteira_digital)
carteira_digital -=75.99
print(carteira_digital)
carteira_digital += 200
print(carteira_digital)

nome = input("insira seu nome.. ")
saudaçao = "ola"+nome
print(saudaçao) 
numero_string = input()
numero_inteiro = int( numero_string )
subtraçao = numero_inteiro - 2
print(subtraçao) """
def quadrado (lado):
    area = lado ** 2
    return area
print(quadrado(30))
def reajuste(salario):
    novo = salario = salario + salario * 0.15
    return novo 
print(reajuste(10000))
def triangulo(base, altura):
    area = (base*altura)/2
    return area
print(triangulo(300, 5))
def grauscelsius(C):
    F = (9*C+160)/5
    return F
print(grauscelsius(100))
def trocadevalores(x, y):
    z=x
    x=y
    y=z
    return x,y
print(trocadevalores(2,3))