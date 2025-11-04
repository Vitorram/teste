def adicionar_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adicionar_clientes("Vitor", lista1)
adicionar_clientes('joao', cliente1)
cliente2 = adicionar_clientes('Anna')
print(cliente1)
print(cliente2) 
