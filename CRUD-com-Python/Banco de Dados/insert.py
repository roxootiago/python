import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "cdd2023",
    database = "escola"
)

meucursor = banco.cursor()

nome1 = "Deide Costa"
telefone1 = "81933149938"
cpf1 = "30912020466"
media1 = 9.3
situacao1 = "a"
status1 = "APROVADO"
FK_Turmas1 = 2

cursor = banco.cursor()
sql = "INSERT INTO aluno (nome,telefone,cpf,media,situacao,status," \
      "Fk_Turmas) VALUES (%s,%s,%s,%s,%s,%s,%s)"
data = (nome1,telefone1,cpf1,media1,situacao1,status1,FK_Turmas1)
cursor.execute(sql,data)
banco.commit()
userid = cursor.lastrowid
print(userid)
cursor.close()
banco.close()