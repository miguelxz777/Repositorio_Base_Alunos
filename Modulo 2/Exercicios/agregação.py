class Midia:
    def __init__(self , titulo :str,artista ):
        self.titulo = titulo
        self.artista = artista
class Musica(Midia):
    def __repr__(self):
        return f"'{self.titulo}'por {self.artista}"
class Playlist:
    def __init__(self,nome:str,musicas: list[Musica]):
        self.nome = nome
        self.musicas = musicas

    def tocar_todas(self):
        print(f"\n tocando a playlist'{self.nome}':")
        for musica in self.musicas:
            print(f" tocando agora:{musica}")

musica_1 = Musica("Jesus chorou,são paulo,fabrica de bico","Racionais MC's")
musica_2 = Musica("Aoa,Favela sinistra,Partiu","MC kekel")
musica_3 = Musica("Mina de Vermelho,tiger preta,por que o homem não chora","MC daleste")

daylist = Playlist ("sua playlist diaria",
                    [musica_1,musica_2,musica_3])
daylist.tocar_todas()
print(musica_1)