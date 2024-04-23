# atividade 2 feita por Alana Soares e Samara Araújo

Classe Animal:
def __init__ (self, nome, idade, especie):
    auto.nome = nome
    auto.idade = idade
    auto.especie = especie

def som (self):
    return f' {self.nome} está emitindo um som: "miau, miau!"'
def informações (self):
    return f' {self.nome}, {self.idade}, {self.especie}, são as informações do {self.nome}'

se __nome__ == "__main__":
animal1 = Animal ("maya", "1 ano", "cachorro")
imprimir (animal1.som ())
print (animal1.informações ())

