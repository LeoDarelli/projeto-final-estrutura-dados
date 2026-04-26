import os
from lista_encadeada import ListaEncadeada
from arvore_bst import ArvoreBST
from grafo import Grafo
import atribuicoes_secretario as sec
import atribuicoes_diretor as dir_ops
import atribuicoes_assistente as ass_ops

CIDADE_ESCOLA = "Guarujá"
CIDADE_INTERMEDIARIA = "Indaiatuba"
CAMINHO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cidades_vizinhas.csv")


def menu_secretario(lista, cidades):
    print("\n-------------- Olá, Secretário(a)! --------------")
    while True:
        print("\nVocê deseja:")
        print("(1) Cadastrar nova pessoa na lista de espera.")
        print("(2) Consultar pessoa cadastrada.")
        print("(3) Ver quantidade de pessoas cadastradas.")
        print("(4) Finalizar execução.")
        opcao = input("Digite sua opção: ").strip()

        if opcao == '1':
            nome = input("Digite o nome da pessoa: ").strip()
            idade = input("Digite a idade: ").strip()
            telefone = input("Digite o telefone: ").strip()
            sec.cadastrar_pessoa(lista, nome, int(idade), telefone, cidades)
            for p in sec.listar_pessoas(lista):
                print(p)
        elif opcao == '2':
            nome = input("Digite o nome da pessoa: ").strip()
            pessoa = sec.consultar_pessoa(lista, nome)
            if pessoa:
                print(pessoa)
            else:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
        elif opcao == '3':
            qtd = sec.contar_pessoas(lista)
            print(f"São {qtd} pessoas na lista de espera.")
        elif opcao == '4':
            break


def menu_diretor(lista, arvore):
    print("\n-------------- Olá, Diretor(a)! --------------")
    while True:
        print("\nVocê deseja:")
        print("(1) Alterar nome, idade ou telefone de pessoa cadastrada.")
        print("(2) Descadastrar pessoa.")
        print("(3) Obter informações da primeira pessoa em ordem alfabética de nome.")
        print("(4) Obter informações da última pessoa em ordem alfabética de nome.")
        print("(5) Confirmar validade da lista de espera e finalizar execução.")
        opcao = input("Digite sua opção: ").strip()

        if opcao == '1':
            nome = input("Digite o nome da pessoa que você quer editar: ").strip()
            pessoa = arvore.buscar(nome)
            if pessoa is None:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
                continue
            print(pessoa)
            campo = input("O que você quer editar? Digite 1 para nome, 2 para idade ou 3 para telefone: ").strip()
            if campo == '1':
                novo_valor = input("Digite o novo nome: ").strip()
                dir_ops.editar_pessoa(lista, arvore, nome, 1, novo_valor)
                print("Dados atualizados com sucesso.")
            elif campo == '2':
                novo_valor = input("Digite a nova idade: ").strip()
                dir_ops.editar_pessoa(lista, arvore, nome, 2, int(novo_valor))
                print("Dados atualizados com sucesso.")
            elif campo == '3':
                novo_valor = input("Digite o novo telefone: ").strip()
                dir_ops.editar_pessoa(lista, arvore, nome, 3, novo_valor)
                print("Dados atualizados com sucesso.")
        elif opcao == '2':
            nome = input("Digite o nome da pessoa que você quer descadastrar: ").strip()
            pessoa = arvore.buscar(nome)
            if pessoa is None:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome está certo?")
                continue
            print(pessoa)
            confirmacao = input(f"Tem certeza que deseja descadastrar {nome}? Digite S ou N: ").strip()
            if confirmacao.upper() == 'S':
                dir_ops.descadastrar_pessoa(lista, arvore, nome)
                print(f"{nome} descadastrado(a) com sucesso.")
        elif opcao == '3':
            pessoa = dir_ops.primeiro_alfabetico(arvore)
            if pessoa:
                print(pessoa)
            else:
                print("Lista de espera vazia.")
        elif opcao == '4':
            pessoa = dir_ops.ultimo_alfabetico(arvore)
            if pessoa:
                print(pessoa)
            else:
                print("Lista de espera vazia.")
        elif opcao == '5':
            print("Fim das atividades sob responsabilidade do(a) Diretor(a).")
            break


def menu_assistente(lista, arvore, grafo):
    print("\n-------------- Olá, Assistente! --------------")
    while True:
        print("\nVocê deseja:")
        print("(1) Ver a menor distância entre a cidade da escola e a cidade de uma pessoa.")
        print("(2) Ver a menor distância da cidade da escola até a cidade da pessoa passando por uma cidade específica.")
        print("(3) Ver dados da(s) pessoa(s) que mora(m) na cidade mais perto da cidade da escola (incluindo distância).")
        print("(4) Finalizar execução.")
        opcao = input("Digite sua opção: ").strip()

        if opcao == '1':
            nome = input("Digite o nome da pessoa cuja cidade te interessa: ").strip()
            pessoa, caminho, custo = ass_ops.menor_distancia(grafo, CIDADE_ESCOLA, nome, arvore)
            if pessoa is None:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome está certo?")
                continue
            print(pessoa)
            print(f"Menor caminho = {caminho} com custo {custo}")
        elif opcao == '2':
            nome = input("Digite o nome da pessoa cuja cidade te interessa: ").strip()
            pessoa, caminho, custo = ass_ops.menor_distancia_passando_por(
                grafo, CIDADE_ESCOLA, CIDADE_INTERMEDIARIA, nome, arvore
            )
            if pessoa is None:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome está certo?")
                continue
            print(pessoa)
            print(f"Menor caminho = {caminho} com custo {custo}")
        elif opcao == '3':
            cidade, distancia, moradores = ass_ops.cidade_mais_proxima_com_moradores(
                grafo, CIDADE_ESCOLA, lista
            )
            if cidade is None:
                print("Lista de espera vazia.")
                continue
            print(f"A cidade mais próxima à cidade da escola que tem moradores na lista de espera (ver abaixo) é {cidade}. Distância = {distancia}")
            for p in moradores:
                print(p)
        elif opcao == '4':
            print("Fim das atividades sob responsabilidade do(a) assistente.")
            break


def main():
    lista = ListaEncadeada()
    grafo = Grafo()
    grafo.carregar_csv(CAMINHO_CSV)
    cidades = sec.obter_cidades_do_csv(CAMINHO_CSV)

    menu_secretario(lista, cidades)

    arvore = ArvoreBST()
    arvore.construir_da_lista(lista)

    menu_diretor(lista, arvore)
    menu_assistente(lista, arvore, grafo)


if __name__ == "__main__":
    main()
