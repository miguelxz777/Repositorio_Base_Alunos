class SalaDeAula:

    def __init__(self, numero: int,capacidade: int):
        self.numero = numero
        self.capacidade = capacidade
        print(f"Sala [self.numero] esta disponivel.")
class Pessoa:
    def __init__(self, nome,idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
class professor:
    def dar_aula(self, sala: SalaDeAula):
        print(f"o prof. {self.nome} de {self.diciplina} esta dando aula na sala{sala.numero}.")


sala_ciencias = SalaDeAula(numero=7 , capacidade = 30)
professor_lazaro = professor(nome = "lazaro",diciplina="ciencias")
professor_lazaro.dar_aula(sala_ciencias)