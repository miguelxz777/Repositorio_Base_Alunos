import sqlite3
try:
    con = sqlite3.connect('bibibliorteca.db')
    cur = con.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS LIVRO (
        idLivro         INTEGER PRIMARY KEY AUTOINCREMENT,
        genero          VARCHAR(50),
        titulo          VARCHAR(50),
        dataPublicação  DATE,
        autor           VARCHAR(200)
    );

    CREATE TABLE IF NOT EXISTS aluno(
        idAluno INTEGER PRIMARY KEY AUTOINCREMENT,
        nome            VARCHAR(255),
        celular         VARCHAR(15),
        turma           CHAR(1)
    );

    CREATE TABLE IF NOT EXISTS emprestimo(
        idEmprestimo    INTEGER PRIMARY KEY AUTOINCREMENT,
        VALOR           REAL,
        idLivro         INTEGER,
        idAluno         INTEGER,
        FOREIGN KEY (idAluno) REFERENCES aluno(idAluno),
        FOREIGN KEY (idLivro) REFERENCES livro(idLivro)
    );

    INSERT INTO aluno(nome, celular, turma) VALUES
        ('pedro henrique', '13426672536', '1'),
        ('Joana Viera', '13426672536', '1'),
        ('Miguel Jose', '13426672536', '1'),
        ('Thiago gabriel', '13426672536', '1'),
        ('Victor Hugo', '13426672536', '1'),
        ('Guilherme Ferreira', '13426672536', '1');

    INSERT INTO livro(genero, titulo, dataPublicação, autor) VALUES
        ('terror', 'IT: a coisa', DATE('now'), 'Stephen King'),
        ('comedia', 'Diario de um banana', DATE('now'), 'Jeff Kinney'),
        ('Quadrinhos', 'Batman absoluto', DATE('now'), 'Scott Snyder');

    INSERT INTO emprestimo(valor, idLivro, idAluno) VALUES
        (30.00, 1, 3),
        (7.00, 2, 6),
        (9.00, 3, 2);
    """)

    con.commit()
    cur.close()

except ConnectionRefusedError as e:
    print('Erro de conexão:', e)
 