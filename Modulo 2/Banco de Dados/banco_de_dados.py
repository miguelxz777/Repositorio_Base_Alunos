import sqlite3
try:
    con = sqlite3.connect("meu_banco.db")
    cur = con.cursor()
    # cur.execute("CREATE TABLE pessoa(id,nome,idade,cpf)"
    cur.execute("INSERT INTO pessoa VALUES(1,'miguel',16,'562.856.746-74')")
    cur.execute("INSERT INTO pessoa VALUES(2,'henzo',12,'562.856.746-73')")
    cur.execute("INSERT INTO pessoa VALUES(3,'eduardo',18,'562.856.746-75')")
    cur.execute("INSERT INTO pessoa VALUES(4,'joao',11,'562.866.746-74')")
    cur.execute("INSERT INTO pessoa VALUES(5,'erick',15,'562.956.746-74')")
    cur.execute("INSERT INTO pessoa VALUES(6,'gabriel',17,'362.856.746-74')")
    cur.execute("INSERT INTO pessoa VALUES(7,'deyvd',14,'562.899.746-74')")
    cur.execute("INSERT INTO pessoa VALUES(8,'corinthians',115,'562.856.756-74')")
    cur.execute("INSERT INTO pessoa VALUES(9,'nadson ferinha',19,'562.856.746-88')")
    cur.execute("INSERT INTO pessoa VALUES(10,'nathanzinho lima',12,'562.856.746-784')")
    cur.execute("DELETE FROM pessoa where Nome = '2'")
    res = cur.execute("SELECT * FROM pessoa")
    pessoas = res.fetchall()
    for p in pessoas:
        print(p)
    cur.close()
    con.commit()

except ConnectionRefusedError as c:
    print('erro de conecção com o banco.')