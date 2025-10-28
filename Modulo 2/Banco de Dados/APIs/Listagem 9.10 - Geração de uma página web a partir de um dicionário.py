filmes={
    "drama": ["Clube da Luta","A Origem","O Silêncio dos Inocentes","Um Sonho de Liberdade","À Espera de um Milagre"],
    "comédia": ["Superbad - É Hoje","Apertem os Cintos... O Piloto Sumiu!","A Morte de Stalin","Se Beber, Não Case!","A Vingança de Uma Mulher"],
    "policial": ["Seven: Os Sete Crimes Capitais""Os Infiltrados""O Grande Lebowski""Prisioneiro do Crime""Os Suspeitos"],
    "guerra": ["Rambo","1917","Até o Último Homem"],
    "terror": ["O Exorcista","Hereditary: O Herdeiro","It: A Coisa","O Iluminado","A Bruxa"],
    "ficcao_cientifica": ["Blade Runner 2049","Matrix","Interstellar","O Homem do Futuro","Minority Report"],
    "animacao": ["Toy Story 3","Coraline e o Mundo Secreto","Up - Altas Aventuras","O Rei Leão","Os Incríveis"],
    "romance": ["Diário de uma Paixão","La La Land: Cantando Estações","Antes do Amanhecer","A Culpa é das Estrelas","O Amor Nos Tempos do Cólera"],
    "aventura": ["Indiana Jones e os Caçadores da Arca Perdida","Jurassic Park","O Senhor dos Anéis: A Sociedade do Anel","Piratas do Caribe: A Maldição do Pérola Negra","As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa"]}

página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title>Filmes</title>
        </head>
        <body> 
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>" % c)
    for e in v:
        página.write("<h2>%s</h2>" % e)
página.write("""
</body>
</html>
""")
página.close()