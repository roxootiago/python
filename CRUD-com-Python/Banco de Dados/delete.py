import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "cdd2023",
    database = "escola"
)

meucursor = banco.cursor()



cursor = banco.cursor()
sql = "delete from aluno where matricula = 7"
cursor.execute(sql)
banco.commit()
userid = cursor.lastrowid
print(userid)
cursor.close()
banco.close()