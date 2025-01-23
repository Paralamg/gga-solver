import numpy as np
from graphs.graph_node import Node
from graphs.graph_arc import Arc


class Graph:
    def __init__(self):
        self.nodes = []
        self.arcs = []
        self.is_normal_result = False

    def add_node(self, node: Node):
        """
        Добавляет узел в граф
        :param node: узел
        """
        self.nodes.append(node)

    def add_arc(self, start: Node, end: Node, model):
        """
        Добавляет дугу в граф
        :param start: узел начала дуги
        :param end: узел конца дуги
        :param model: расчетная модель узла
        """
        arc = Arc(start, end, model)
        self.arcs.append(arc)

    def get_incidence_matrix(self) -> np.array:
        """
        Создает матрицу инцидентности

        :return: матрица инцидентности
        """
        pass

    def get_m(self) -> int:
        """
        Возвращает количество узлов в графе

        :return: количество узлов в графе
        """
        pass

    def get_n(self) -> int:
        """
        Возвращает количество дуг в графе

        :return: количество дуг в графе
        """
        pass

    def get_k(self) -> int:
        """
        Возвращает количество узлов с заданным притоком/оттоком
        :return:количество узлов с заданным притоком/оттоком
        """
        pass

    def get_sorted_nodes(self) -> list[Node]:
        """
        Возвращает список узлов отсортированных по следующему правилу:
        узлы с известным притоком/оттоком находятся вначале списка,
        узлы с известным давлением

        :return: отсортированный список узлов
        """
        pass



