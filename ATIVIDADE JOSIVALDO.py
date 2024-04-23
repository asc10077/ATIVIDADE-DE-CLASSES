Classe Veiculo :
def __init__(self, marca, modelo):
         auto.marca = marca
         auto.modelo = modelo

def frear (self):
        return(f"{self.marca} {self.modelo} o veiculo está freando.")

def acelerar (self):
        return (f"{self.marca} {self.modelo} o veiculo está acelerando.")

Classe Carro (Veiculo):
def __init__(self, marca, modelo, cor):
      super (). __init__(marca, modelo)
      auto.cor = cor
def abrir_porta (self):
     return (f" as portas do {self.marca} {self.modelo} {self.cor} estão abertas")

Classe Moto (Veiculo):
def __init__(self, marca, modelo, cilindrada):
    super (). __init__ (marca, modelo)
    auto.cilindrada = cilindrada
def empinar(self):
     return (f"{self.marca} {self.modelo} {self.cilindrada} está empinando")

se __nome__ == "__main__":
    carro = Carro (" Fiat", "Uno", "cinza")
imprimir (carro.frear ())
imprimir (carro.acelerar ())
print (carro.abrir_porta ())

moto = Moto ("Ronda", "CG 125", "125 cc")
imprimir (moto.empinar ())
imprimir (moto.acelerar ())

