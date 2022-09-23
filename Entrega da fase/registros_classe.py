import mysql.connector

class Chamado:
        
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ' ',
        database = 'ouvidoria'   
        )

    cursor = connection.cursor()

    def __init__(self):
        pass
    
    def cadastrar(self, tipo, conteudo):
        sql = 'INSERT INTO chamados(tipo, conteudo) values (%s, %s)'
        data = (tipo, conteudo)
        
        self.cursor.execute(sql, data)
        self.connection.commit()
                
        return('\nChamado inserido\n')

    def listCham(self, tipo):
         
        sql = f'SELECT * FROM chamados WHERE tipo="{tipo}"'
        print(f'{tipo}: \n')
        self.cursor.execute(sql)
        listacham = self.cursor.fetchall()
        for i in listacham:
            print(i)
        print('\nFim\n')
     
        
    
    def removeChamado(self, id):
        sql = f'DELETE FROM chamados WHERE ID ="{id}"' 
        self.cursor.execute(sql)      
        print('\nFinalizado\n')

         
