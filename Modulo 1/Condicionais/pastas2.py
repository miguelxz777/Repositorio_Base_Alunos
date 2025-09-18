minha_senha = "24459d"
def verificar_senha(nova_senha):
    if ler(nova_senha) > 6:
        print("valida")
    else:
        print("invalida")