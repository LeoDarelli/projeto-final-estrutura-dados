import random
from pessoa import Pessoa


def obter_cidades_do_csv(caminho_csv):
    cidades = set()
    with open(caminho_csv, 'r', encoding='utf-8') as f:
        for linha in f:
            partes = linha.strip().split(';')
            if len(partes) == 3:
                cidades.add(partes[0].strip())
                cidades.add(partes[1].strip())
    return list(cidades)


def cadastrar_pessoa(lista, nome, idade, telefone, cidades):
    cidade = random.choice(cidades)
    pessoa = Pessoa(nome, idade, telefone, cidade)
    lista.inserir(pessoa)
    return pessoa


def consultar_pessoa(lista, nome):
    return lista.buscar(nome)


def contar_pessoas(lista):
    return lista.contar()


def listar_pessoas(lista):
    return lista.listar()
