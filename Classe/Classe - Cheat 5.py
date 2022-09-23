class Bichinho:
    nome = ""
    fome = 0
    saúde = 10
    idade = 0

    def mudarNome(self, nom, fom, sau, idad):
        self.nome = nom
        self.fome = fom
        self.saude = sau
        self.idade = idad
        return(self.nome, self.fome, self.saude, self.idade)


    
vBichin = Bichinho()
print(vBichin.mudarNome('Caramelo', 6, 8, 1))
