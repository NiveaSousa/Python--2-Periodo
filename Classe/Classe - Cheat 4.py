from filecmp import clear_cache


class Calculadora:
    A = 0.0
    B = 0.0

    def valores(self, A, B):
        self.A = A
        self.B = B

    def somar(self):
        soma = self.A+self.B
        print(soma)

    def subtrair(self):
        sub = self.A-self.B
        print(sub)
    
    def multiplicar(self):
        mult = self.A*self.B
        print(mult)

    def dividir(self):
        div = self.A/self.B
        print(div)

calc = Calculadora()
calc.valores(10,6)
calc.somar()
calc.subtrair()
calc.multiplicar()
calc.dividir()
