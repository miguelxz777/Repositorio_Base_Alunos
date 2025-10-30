 CREATE TABLE IF NOT EXISTS jogador(
    idJogador                   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome                        VARCHAR(50),
    nivel                       INTEGER,
    pontos                      INTEGER,
    moedas_do_jogo              INTEGER
);

CREATE TABLE IF NOT EXISTS carro(
    idCarro                     INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome_do_carro               VARCHAR(30),
    velocidade_maxima           INTEGER,
    tempo_de_0_100              INTEGER,
    valor_do_carro              REAL
);

CREATE TABLE IF NOT EXISTS upgrade_carro(
    idUpgrade                   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_do_upgrade             VARCHAR(50),
    valor_do_upgrade            REAL,
    efeito_do_upgrade           VARCHAR(50),
    idCarro                     INTEGER,
    idJogador                   INTEGER,
    FOREIGN KEY (idCarro) REFERENCES carro(idCarro),
    FOREIGN KEY (idJogador) REFERENCES jogador(idJogador)
);

CREATE TABLE IF NOT EXISTS pista(
    idPista                     INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_da_pista               VARCHAR(50),
    localizacao_da_pista        VARCHAR(50),
    tamanho_da_pista            INTEGER
);

CREATE TABLE IF NOT EXISTS corrida(
    idCorrida                   INTEGER PRIMARY KEY AUTOINCREMENT,
    idJogador                   INTEGER,
    idCarro                     INTEGER,
    idPista                     INTEGER,
    tempo_da_corrida            VARCHAR(20),
    posicao_final               INTEGER,
    FOREIGN KEY (idJogador) REFERENCES jogador(idJogador),
    FOREIGN KEY (idCarro) REFERENCES carro(idCarro),
    FOREIGN KEY (idPista) REFERENCES pista(idPista)
);
