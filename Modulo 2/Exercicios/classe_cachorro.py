from classe_pai import Animal 
class Cachorro(Animal):
    def __init__(self,nome,raça):
        super().__init__(nome)
        self.raca = raça
    
    def fazer_som(self):
        print(f"{self.nome} esta latindo: Au Au!")

    def abanar_rabo(self):
        print(f"{self.nome}esta abanando o rabo")
    