import numpy as np


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def get_incidence_matrix(self):
        n = self.get_n()
        m = self.get_m()
        k = self.get_k()
        sorted_nodes = self.get_sorted_nodes()
        A = np.zeros((m, n))
        for num, way in enumerate(data_edge[['input_nodes', 'output_nodes']].values):
            A[way[0], num] = 1
            A[way[1], num] = -1
        A = A[data_node.index]  # Сортировка по индексам
        A1 = A[:k]  # Матрица инцидентности для узлов с известными расходами
        A2 = A[k:m]  # Матрица инцидентности для узлов с не известными расходами

    def get_m(self):
        return len(self.nodes)

    def get_n(self):
        return len(self.edges)

    def get_k(self):
        node_with_sign_flow = [node for node in self.nodes if node.sign == 'flow']
        return len(node_with_sign_flow)

    def get_sorted_nodes(self):
        node_with_sign_flow = [node for node in self.nodes if node.sign == 'flow']
        node_with_sign_pressure = [node for node in self.nodes if node.sign == 'pressure']
        return node_with_sign_flow.append(node_with_sign_pressure)



