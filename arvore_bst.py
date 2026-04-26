class NoBST:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.esquerda = None
        self.direita = None


class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def construir_da_lista(self, lista_encadeada):
        self.raiz = None
        for pessoa in lista_encadeada.listar():
            self.inserir(pessoa)

    def inserir(self, pessoa):
        self.raiz = self._inserir(self.raiz, pessoa)

    def _inserir(self, no, pessoa):
        if no is None:
            return NoBST(pessoa)
        if pessoa.nome < no.pessoa.nome:
            no.esquerda = self._inserir(no.esquerda, pessoa)
        elif pessoa.nome > no.pessoa.nome:
            no.direita = self._inserir(no.direita, pessoa)
        return no

    def buscar(self, nome):
        return self._buscar(self.raiz, nome)

    def _buscar(self, no, nome):
        if no is None:
            return None
        if nome == no.pessoa.nome:
            return no.pessoa
        elif nome < no.pessoa.nome:
            return self._buscar(no.esquerda, nome)
        else:
            return self._buscar(no.direita, nome)

    def remover(self, nome):
        self.raiz, removido = self._remover(self.raiz, nome)
        return removido

    def _remover(self, no, nome):
        if no is None:
            return no, False
        removido = False
        if nome < no.pessoa.nome:
            no.esquerda, removido = self._remover(no.esquerda, nome)
        elif nome > no.pessoa.nome:
            no.direita, removido = self._remover(no.direita, nome)
        else:
            removido = True
            if no.esquerda is None:
                return no.direita, removido
            elif no.direita is None:
                return no.esquerda, removido
            # Dois filhos: substitui pelo sucessor (mínimo da subárvore direita)
            sucessor = self._no_minimo(no.direita)
            no.pessoa = sucessor.pessoa
            no.direita, _ = self._remover(no.direita, sucessor.pessoa.nome)
        return no, removido

    def _no_minimo(self, no):
        while no.esquerda:
            no = no.esquerda
        return no

    def minimo(self):
        if self.raiz is None:
            return None
        return self._no_minimo(self.raiz).pessoa

    def maximo(self):
        if self.raiz is None:
            return None
        no = self.raiz
        while no.direita:
            no = no.direita
        return no.pessoa
