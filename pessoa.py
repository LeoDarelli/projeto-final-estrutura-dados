class Pessoa:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade

    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Telefone: {self.telefone} | Cidade: {self.cidade}"
