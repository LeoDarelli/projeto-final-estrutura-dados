import heapq


class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def _adicionar_vertice(self, cidade):
        if cidade not in self.adjacencia:
            self.adjacencia[cidade] = []

    def adicionar_aresta(self, cidade1, cidade2, distancia):
        self._adicionar_vertice(cidade1)
        self._adicionar_vertice(cidade2)
        self.adjacencia[cidade1].append((cidade2, distancia))
        self.adjacencia[cidade2].append((cidade1, distancia))

    def carregar_csv(self, caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            for linha in f:
                partes = linha.strip().split(';')
                if len(partes) == 3:
                    cidade1 = partes[0].strip()
                    cidade2 = partes[1].strip()
                    try:
                        distancia = int(partes[2].strip())
                        self.adicionar_aresta(cidade1, cidade2, distancia)
                    except ValueError:
                        pass

    def dijkstra(self, origem):
        distancias = {cidade: float('inf') for cidade in self.adjacencia}
        anteriores = {cidade: None for cidade in self.adjacencia}
        if origem not in distancias:
            return distancias, anteriores
        distancias[origem] = 0
        heap = [(0, origem)]

        while heap:
            dist_atual, cidade_atual = heapq.heappop(heap)
            if dist_atual > distancias[cidade_atual]:
                continue
            for vizinho, peso in self.adjacencia.get(cidade_atual, []):
                nova_dist = dist_atual + peso
                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    anteriores[vizinho] = cidade_atual
                    heapq.heappush(heap, (nova_dist, vizinho))

        return distancias, anteriores

    def _reconstruir_caminho(self, anteriores, origem, destino):
        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            atual = anteriores.get(atual)
        caminho.reverse()
        if not caminho or caminho[0] != origem:
            return []
        return caminho

    def menor_caminho(self, origem, destino):
        distancias, anteriores = self.dijkstra(origem)
        custo = distancias.get(destino, float('inf'))
        caminho = self._reconstruir_caminho(anteriores, origem, destino)
        return caminho, custo

    def menor_caminho_passando_por(self, origem, intermediario, destino):
        dist1, ant1 = self.dijkstra(origem)
        caminho1 = self._reconstruir_caminho(ant1, origem, intermediario)
        custo1 = dist1.get(intermediario, float('inf'))

        dist2, ant2 = self.dijkstra(intermediario)
        caminho2 = self._reconstruir_caminho(ant2, intermediario, destino)
        custo2 = dist2.get(destino, float('inf'))

        if not caminho1 or not caminho2:
            return [], float('inf')

        caminho_total = caminho1 + caminho2[1:]
        custo_total = custo1 + custo2
        return caminho_total, custo_total

    def obter_cidades(self):
        return list(self.adjacencia.keys())
