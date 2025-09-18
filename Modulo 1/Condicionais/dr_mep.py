def atendimentos():
    valor_total = 0
    raça = input("digite uma raça: ")
    raças = ['pug','pastor_alemão','labrador']
    if raça in raças:
        if raça == "pug":
            valor_total = 70.99
            print(valor_total)
        elif raça  == "pastor_alemão":
            valor_total = 120.99
            print(valor_total)
        elif raça == "labrador":
            valor_total = 110.99
            print(valor_total)
    else:
        print("atendimento não dispomivel")
atendimentos()