class Passaro():
    def __init__(self,tamanho,cores,espécie,sexo,habitat):
        self.tamanho = tamanho
        self.cores = cores
        self.espécie = espécie
        self.sexo = sexo
        self.habitat = habitat

    def cantar(self):
        return print(f'sou um {self.espécie} cantando uma bela cançao')
    def voar(self):
        return print(f'batendo as asas e: voando...')

passaro1 = Passaro(0.14,['marrom','branco','cinza'],'pardal ', 'm')
passaro1.cantar()
passaro1.voar()
passaro2 = Passaro(0.70[' preto','cinza ','azulado'],'corvo', 'm')
passaro2.cantar()
passaro2.voar()
passaro3 = Passaro(1.40,['azul','amarelo','vermelho'],'arara', 'm')
passaro3.cantar()
passaro3.voar()
passaro4 = Passaro(0.37,['verde','avermelhado','roxo'],'pomba', 'm')
passaro4.cantar()
passaro4.voar()