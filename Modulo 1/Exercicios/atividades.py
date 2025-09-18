"""def caixa_eletronico():
    saldo = int(input("digite o saldo bancario"))
    saque = int(input("digite o valor de saque"))
    if saldo >= saque:
        saldo -= saque
        print("voce realizou um saque com sucesso", saldo)
    else:
        print("voçe não possui saldo sulficiente para realizar essa operação")
caixa_eletronico()
def realizar_deposito():
    saldo_atual = int(input("digite o saldo atual da conta"))
    valor_deposito = int(input("digite o valor a ser depositado"))
    novo_saldo = saldo_atual + valor_deposito
    print("deposito realizado com sucesso!", novo_saldo)
realizar_deposito()"""
def valores():
    valor_parte = float(input("insira o valor parte: "))
    porcentagem = float(input("insira o valor da porcentagem"))
    if (porcentagem <= 0.0):
        print("insira um valor maior que zero")
    else:
        valor_total = valor_parte * (porcentagem /100)
        print(valor_total)
valores()