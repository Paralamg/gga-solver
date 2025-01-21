import numpy as np
from graphs.graph_node import Node
from graphs.graph_arc import Arc


class Graph:
    def __init__(self):
        self.nodes = []
        self.arcs = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def add_arc(self, start: Node, end: Node, model):
        
        arc = Arc(start, end, model)
        self.arcs.append(arc)

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



