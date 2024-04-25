class Veiculo:
    def __init__(self, marca, modelo): 
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f'{self.marca} acelera')

    def frear(self):
        print('o carro freia')

modelo = input('Digite o nome do modelo: ')
marca = input('Digite a marca do veículo: ')

carro = Veiculo(marca, modelo)
carro.acelerar()
carro.frear()