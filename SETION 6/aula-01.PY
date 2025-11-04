class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def mostrar(self):
        print(f'nome: {self.nome}, sobrenome:{self.sobrenome}')
    
p1 = Pessoa('Vitor', 'Ramos')
p1.mostrar()
