class No:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def inserir(self, pessoa):
        novo = No(pessoa)
        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self._tamanho += 1

    def buscar(self, nome):
        atual = self.cabeca
        while atual:
            if atual.pessoa.nome == nome:
                return atual.pessoa
            atual = atual.proximo
        return None

    def remover(self, nome):
        if self.cabeca is None:
            return False
        if self.cabeca.pessoa.nome == nome:
            self.cabeca = self.cabeca.proximo
            self._tamanho -= 1
            return True
        atual = self.cabeca
        while atual.proximo:
            if atual.proximo.pessoa.nome == nome:
                atual.proximo = atual.proximo.proximo
                self._tamanho -= 1
                return True
            atual = atual.proximo
        return False

    def contar(self):
        return self._tamanho

    def listar(self):
        resultado = []
        atual = self.cabeca
        while atual:
            resultado.append(atual.pessoa)
            atual = atual.proximo
        return resultado
