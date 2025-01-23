import math
from graphs.graph import Graph
import numpy as np

class GgaSolver:

    def __init__(self):
        self.graph = None
        self.ACCURACY = 1000

    def solve(self, graph: Graph):
        """
        Производит расчет ГТС методом глобального градиента

        :param graph: расчетный граф
        """
        self.graph = graph
        self.__initialize()
        self.__main_loop()

    def __initialize(self):
        """
        Инициализирует метод глобального градиента:
        1. Задает постоянные величины
        2. Задает начальное приближение по расходу и давлению
        """
        self.m = self.graph.get_m()
        self.n = self.graph.get_n()
        self.k = self.graph.get_k()
        self.A = self.graph.get_incidence_matrix()
        self.A1 = self.A[:self.k]
        self.A2 = self.A[self.k:]
        self.X_vector = np.random.rand(self.n)
        self.sorted_nodes = self.graph.get_sorted_nodes()
        self.P_vector = np.array([node.pressure* node.pressure for node in self.sorted_nodes])
        self.Q_vector = np.array([node.flow_rate for node in self.sorted_nodes])

    def __main_loop(self):
        """
        Выполняет итерационный алгоритм:
        1. Определяет значение вектор-функции F(x) и обратную матрицу F'(x)^-1
        2. Выполняет шаг по давлению
        3. Выполняет шаг по расходу
        4. Обновляет значение давления и притока/оттока в узле
        5. После цикла обновляет расход на дугах
        """
        step = 0
        mistake = math.inf
        while mistake > self.ACCURACY and step < 100:
            # Найти F(x), F`(x) и матрицу Максвела в соответсвии с формулами 
            f_vector = self.__get_f_vector(self.X_vector)
            f_diff_inv = self.__get_f_diff_inv(self.X_vector)
            maxwell = self.A1 @ f_diff_inv @ self.A1.T  # (m-k)x(m-k)

            # Сделать шаг итераци в соответсвии с выведенными формулами. Получить вектор давлений и расходов по ребрам
            self.P_vector[:self.k] = (np.linalg.inv(maxwell) @
                                      (self.Q_vector[:self.k] - self.A1 @ self.X_vector - self.A1 @ f_diff_inv @
                                       (self.A2.T @ self.P_vector[self.k:] - f_vector)))
            self.X_vector = self.X_vector + f_diff_inv @ (self.A.T @ self.P_vector - f_vector)
            self.Q_vector[self.k:] = self.A2 @ self.X_vector

            self.__update_node(self.P_vector, self.Q_vector)

            # Опеределить ошибку
            mistake = np.abs(self.A.T @ self.P_vector - f_vector).max()
            step += 1
        else:
            self.__update_arc(self.X_vector)
            if mistake < self.ACCURACY:
                self.graph.is_normal_result = True
            else:
                print("Error")
        

    def __get_f_vector(self, x_vector: np.array) -> np.array:
        return np.array([arc.get_pressure_losses(flow_rate) for arc, flow_rate in zip(self.graph.arcs, x_vector)])

    def __get_f_diff_inv(self, x_vector: np.array) -> np.array:
        f_diff_inv = np.zeros((self.n, self.n))
        for i in range(self.n):
            f_diff_inv[i, i] = 1 / self.graph.arcs[i].get_pressure_derivatives(x_vector[i])
        return f_diff_inv

    def __update_node(self, p_vector: np.array, q_vector: np.array):
        p_vector = np.sqrt(p_vector[:self.k])
        q_vector = q_vector[self.k:]
        for node, pressure in zip(self.sorted_nodes[:self.k], p_vector):
            node.pressure_calculated = pressure

        for node, flow_rate in zip(self.sorted_nodes[self.k:], q_vector):
            node.flow_rate_calculated = flow_rate

    def __update_arc(self, x_vector: np.array):
        for arc, flow_rate in zip(self.graph.arcs, x_vector):
            arc.flow_rate_calculated = flow_rate

