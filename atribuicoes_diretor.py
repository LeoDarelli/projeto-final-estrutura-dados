def editar_pessoa(lista, arvore, nome, campo, novo_valor):
    pessoa = arvore.buscar(nome)
    if pessoa is None:
        return False

    if campo == 1:
        # Nome é a chave da BST: remover, atualizar e reinserir
        arvore.remover(nome)
        pessoa.nome = novo_valor
        arvore.inserir(pessoa)
        # A lista encadeada aponta para o mesmo objeto Pessoa, então já reflete a mudança
    elif campo == 2:
        pessoa.idade = novo_valor
    elif campo == 3:
        pessoa.telefone = novo_valor

    return True


def descadastrar_pessoa(lista, arvore, nome):
    if arvore.buscar(nome) is None:
        return False
    arvore.remover(nome)
    lista.remover(nome)
    return True


def primeiro_alfabetico(arvore):
    return arvore.minimo()


def ultimo_alfabetico(arvore):
    return arvore.maximo()
