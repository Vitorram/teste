class Carro:
    def __init__(self, nome):
        self.nome = nome
    def acelerar(self):
        print(f'{self.nome} esta acelerando...')
    
fusca = Carro('fusca')
fusca.acelerar()
celta = Carro('celta')
celta.acelerar()
    

