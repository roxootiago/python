import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "cdd2023",
    database = "escola"
)

meucursor = banco.cursor()
pesquisa = "select * from aluno"
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()

for x in resultado:
    print(x)

meucursor.close()
banco.close()