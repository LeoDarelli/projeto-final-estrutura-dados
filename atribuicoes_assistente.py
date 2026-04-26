def menor_distancia(grafo, cidade_escola, nome_pessoa, arvore):
    pessoa = arvore.buscar(nome_pessoa)
    if pessoa is None:
        return None, None, None
    caminho, custo = grafo.menor_caminho(cidade_escola, pessoa.cidade)
    return pessoa, caminho, custo


def menor_distancia_passando_por(grafo, cidade_escola, cidade_intermediaria, nome_pessoa, arvore):
    pessoa = arvore.buscar(nome_pessoa)
    if pessoa is None:
        return None, None, None
    caminho, custo = grafo.menor_caminho_passando_por(cidade_escola, cidade_intermediaria, pessoa.cidade)
    return pessoa, caminho, custo


def cidade_mais_proxima_com_moradores(grafo, cidade_escola, lista):
    pessoas = lista.listar()
    if not pessoas:
        return None, None, []

    cidades_moradores = {}
    for p in pessoas:
        if p.cidade not in cidades_moradores:
            cidades_moradores[p.cidade] = []
        cidades_moradores[p.cidade].append(p)

    distancias, _ = grafo.dijkstra(cidade_escola)

    menor_dist = float('inf')
    cidade_mais_proxima = None
    for cidade in cidades_moradores:
        d = distancias.get(cidade, float('inf'))
        if d < menor_dist:
            menor_dist = d
            cidade_mais_proxima = cidade

    moradores = cidades_moradores.get(cidade_mais_proxima, [])
    return cidade_mais_proxima, menor_dist, moradores
