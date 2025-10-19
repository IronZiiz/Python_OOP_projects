# 1-Crie uma classe chamada Veiculo com um método abstrato chamado ligar.

from abc import ABC, abstractclassmethod

class Veiculo:
    @abstractclassmethod
    def ligar(self):
        raise NotImplementedError("Subclasses devem implementar este método")
# 2-No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractclassmethod
    def ligar(self):
        raise NotImplementedError("Subclasses devem implementar este método")
# 3-Crie uma nova classe chamada Carro que herda da classe Veiculo.
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)

    def ligar(self):
        return f"O carro {self.marca} {self.modelo} está ligado."
    
# 4-No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar(self):
        return f"O carro {self.marca} {self.modelo} está ligado."

# 5-Em um arquivo chamado main.py, importe a classe Carro.
# 6-No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e co