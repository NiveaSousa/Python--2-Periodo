class Retangulo:
    ladoA = 0
    ladoB = 0

    def mudarLado(self, A, B):
        self.ladoA = A
        self.ladoB = B
        return(self.ladoA, self.ladoB)

    def areaR(self):
        area = self.ladoA*self.ladoB
        print(area)

    
qRetan = Retangulo()
print(qRetan.mudarLado(3,4))
qRetan.areaR()
