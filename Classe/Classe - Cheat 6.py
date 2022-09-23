class Macaco:
    nome = ''

   
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def trocaNome(self, troca):
        self.nome = troca
        print(self.nome)
    def comer(self, A):
        self.bucho.append(A)
    def verBucho(self):
        print(self.bucho)
    def digerir(self):
        del self.bucho[0]



macaco1 = Macaco('macaco1')
macaco2 = Macaco('macaco2')

macaco1.trocaNome("Juanito")
macaco1.comer("Banana")
macaco1.comer("Manga")
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()


macaco2.trocaNome("Alvaro")
macaco2.comer("Manga")
macaco2.comer("Banana")
macaco2.verBucho()
macaco2.digerir()
macaco2.verBucho()
