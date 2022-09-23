import mysql.connector

    
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '190709-Nss',
    database = 'ouvidoria'
)

cursor = connection.cursor()

sql = 'INSERT INTO chamados(autor, tipo, conteudo) values (%s, %s, %s)'
data = ('Diego', 'Elogio', 'Muito bom o app')

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()

print('ID do novo usuário', userid)