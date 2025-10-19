#1 Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
#  Inicie o atributo ativo como False por padrão.

#2 Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem
#  formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas
#  instâncias.

#3 Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define
#  o atributo ativo como True. Crie uma instância da classe, chame o método de classe e 
# imprima o valor de ativo.

#4 Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na
#  criação de atributos. Utilize propriedades, se necessário.

#5 Crie uma instância da classe e imprima o valor da propriedade titular.

#6 Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos.
#  Instancie 3 objetos desta classe e atribua valores aos seus atributos através
#  do método construtor.

#7 Crie um método de classe para a conta ClienteBanco.

class ContaBancaria:
    def __init__(self, titular = '', saldo = 0): 
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    @classmethod
    def ativar_conta(cls, conta): 
        conta._ativo = True

    def __str__(self): 
        return f'Nome do(a) titular:{self.titular} | Saldo: {self.saldo}'

    @property
    def ativo(self): 
        return '✅' if self._ativo else '❌'
    
conta1 = ContaBancaria(titular='Alice', saldo=1000)
conta2 = ContaBancaria(titular='Bob', saldo=500)
ContaBancaria.ativar_conta(conta2)  
print(conta2.ativo)

# Imprimindo as instâncias
print(conta1)
print(conta2)

#6 e #7 

class ClienteBanco:
    def __init__(self, titular='', cpf='', cnpj='', endereco='', idade=0):
        self.endereco = endereco
        self.idade = self._formatar_idade(idade)
        self.titular = self._formatar_titular(titular)
        self.cpf = self._formatar_cpf(cpf)
        self.cnpj = self._formatar_cnpj(cnpj)

    def _formatar_titular(self, titular):
        return ' '.join(word.capitalize() for word in titular.strip().split())
    
    def _formatar_idade(self, idade):
        """Garante que a idade seja inteiro e maior ou igual a 18"""
        try:
            idade_int = int(idade)
        except ValueError:
            raise TypeError("Idade deve ser um número inteiro")
        
        if idade_int < 18:
            raise ValueError("Idade deve ser maior ou igual a 18 anos")
        
        return idade_int        

    def _formatar_cpf(self, cpf):
        """
        Formata CPF no padrão XXX.XXX.XXX-XX
        Aceita string ou número inteiro, com ou sem formatação.
        """
        numeros = ''.join(filter(str.isdigit, str(cpf)))
        
        numeros = numeros.zfill(11)

        if len(numeros) != 11:
            raise ValueError("CPF deve ter 11 dígitos")

        # Formata
        return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"


    def _formatar_cnpj(self, cnpj):
        """
        Formata CNPJ no padrão XX.XXX.XXX/XXXX-XX
        Aceita string ou número inteiro, com ou sem formatação.
        """
        numeros = ''.join(filter(str.isdigit, str(cnpj)))

        numeros = numeros.zfill(14)

        if len(numeros) != 14:
            raise ValueError("CNPJ deve ter 14 dígitos")

        return f"{numeros[:2]}.{numeros[2:5]}.{numeros[5:8]}/{numeros[8:12]}-{numeros[12:]}"


    def __str__(self):
        if self.cpf != '000.000.000-00':
         return f'Titular da Conta: {self.titular} | CPF: {self.cpf}'
        else:
         return f'Titular da Conta: {self.titular} | CNPJ: {self.cnpj}'
        
cliente1 = ClienteBanco(titular="Thiago Zilli", cpf=12345678901, idade=30)
cliente2 = ClienteBanco(titular="Empresa XYZ", cnpj=11222333000181, idade=18)
cliente3 = ClienteBanco(titular="João Silva", cpf="987.654.321-00", idade="22")

print(cliente1)
print(cliente2)
print(cliente3)