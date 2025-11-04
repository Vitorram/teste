import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

nome = input("digite seu nome: ")
idade = input("Digite a sua idade: ")
p1 = Pessoa(nome, idade)

with open('pessoas.json', 'w') as a:
    json.dump(p1.__dict__, a,indent=2)



