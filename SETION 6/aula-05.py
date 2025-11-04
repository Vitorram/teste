class Caneta: 
    def __init__(self, cor):
        self.cor_nome = cor

    @property
    def cor(self):
        return self.cor_nome



caneta = Caneta('azul')
print(caneta.cor)