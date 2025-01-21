import numpy as np


class Graph:
    def __init__(self):
        self.nodes = []
        self.arcs = []

    def get_incidence_matrix(self) -> np.array:
        m = self.get_m()
        n = self.get_n()
        A = np.zeros((m, n))
        sorted_nodes = self.get_sorted_nodes()
        for num, arc in enumerate(self.arcs):
            A[sorted_nodes.index(arc.start), num] = 1 
            A[sorted_nodes.index(arc.end), num] = -1
        return A

    def get_m(self) -> int:
        return len(self.nodes)

    def get_n(self) -> int:
        return len(self.arcs)

    def get_k(self) -> int:
        node_with_sign_flow = [node for node in self.nodes if node.sign == 'flow']
        return len(node_with_sign_flow)

    def get_sorted_nodes(self) -> list:
        node_with_sign_flow = [node for node in self.nodes if node.sign == 'flow']
        node_with_sign_pressure = [node for node in self.nodes if node.sign == 'pressure']
        return node_with_sign_flow.append(node_with_sign_pressure)



