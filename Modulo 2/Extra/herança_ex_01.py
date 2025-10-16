class Personagem():
    def __init__(self,olhos, altura,profissão,nome,carro):
        self.olhos = olhos
        self.altura= altura
        self.profissão = profissão
        self.nome = nome
        self.carro = carro

    def piloto(self):
        return print(' É um motorista talentoso, e piloto de fuga')
    def armas(self):
        return print('atirador experiente')
    def mecanica(self):
        return print('Tornou-se um mecânico habilidoso, especialmente com carros da marca Nissan,')
    def estrategias(self):
        return print('Como ex-agente, ele sabe como planejar e executar missões')
    def tuning(self):
        return print('Demonstra interesse em tuning de carros')
