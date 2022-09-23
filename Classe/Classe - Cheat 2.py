class Quadrado:
    t_lado = 0

    def mudarLado(self, lado):
        self.t_lado = lado
        return(self.t_lado)

    def areaQ(self):
        area = self.t_lado**2
        print(area)

    
qQuadrado = Quadrado()
print(qQuadrado.mudarLado(2))
qQuadrado.areaQ()
