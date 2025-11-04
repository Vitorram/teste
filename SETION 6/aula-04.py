class Pessoa:
    ano_atual = 2025
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def ano(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('vitor', 20)
p1.__dict__['outra'] = 'coisa'
del p1.__dict__['outra']
print(p1.__dict__)
p1.__dict__['nome']
print(p1.__dict__)