class Bola:
    cor = 'azul'
    circunferencia = 0.0
    material = ''

    def mostraCor(self):
        print(self.cor)

    def trocaCor(self, troca):
        self.cor = troca


nBola = Bola()
nBola.mostraCor()
nBola.trocaCor('verde')
nBola.mostraCor()