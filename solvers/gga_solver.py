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
        pass

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
            break
        else:
            pass
        

    def __get_f_vector(self, x_vector: np.array) -> np.array:
        pass

    def __get_f_diff_inv(self, x_vector: np.array) -> np.array:
        pass

    def __update_node(self, p_vector: np.array, q_vector: np.array):
        pass

    def __update_arc(self, x_vector: np.array):
        pass

