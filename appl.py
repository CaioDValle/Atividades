class Animal:
    def __init__(self,nome):
        self.nome=nome
    def fazer_som(self):
        print ('O animal faz algum som.')

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

        def fazer_som(self):
            print ('o cachorro faz au au!')
        
