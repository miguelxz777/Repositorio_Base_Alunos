class SalaDeAula:

    def __init__(self, numero: int,capacidade: int):
        self.numero = numero
        self.capacidade = capacidade
        print(f"Sala [self.numero] esta disponivel.")

class professor:
    def dar_aula(self, sala: SalaDeAula):
        print(f"o prof. {self.nome} de {self.diciplina} esta dando aula na sala{sala.numero}.")