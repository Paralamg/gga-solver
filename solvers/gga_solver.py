import math
from graphs.graph import Graph
import numpy as np


class GGASolver:
    def __init__(self):
        pass

    def solve(self, graph: Graph):
        self.graph = graph
        self.initialize()
        self.main_loop()
        
        
    def initialize(self):
        self.m = self.graph.get_m()
        self.n = self.graph.get_n()
        self.k = self.graph.get_k()
        self.A = self.graph.get_incidence_matrix()
        self.A1 = self.A[:self.k] # Взять первые k строк матрицы A
        self.A2 = self.A[self.k:]
        self.X_vector = np.random.rand(self.n)
        sorted_nodes = self.graph.get_sorted_nodes()
        self.P_vector = [node.pressure for node in sorted_nodes]
        self.Q_vector = [node.flow_rate for node in sorted_nodes]
        

    def main_loop(self):
        step = 0
        mistake = math.inf
        while mistake > self.ACCURACY and step < 100:
            # Найти F(x), F`(x) и матрицу Максвела в соответсвии с формулами 
            F_vector = self.get_F_vector(self.X_vector)
            F_diff_inv = self.get_F_diff_inv(self.X_vector)
            maxvel = self.A1 @ F_diff_inv @ self.A1.T # (m-k)x(m-k)
            
            # Сделать шаг итераци в соответсвии с выведенными формулами. Получить вектор давлений и расходов по ребрам
            self.P_vector[:self.k] = np.linalg.inv(maxvel) @ (self.Q_vector[:self.k] - self.A1 @ self.X_vector - 
                                                              self.A1 @ F_diff_inv @ (self.A2.T @ self.P_vector[self.k:] - F_vector))
            self.X_vector = self.X_vector + F_diff_inv @ (self.A.T @ self.P_vector - F_vector)

            # Обновить диагональную матрицу расходов и матрицу коэффициентов idem, перед которой обновим давления на гранях
            for i in range(self.n):
                # Обновление давления в соответсвии с номером узла, который соответсвует индексу data_node
                self.graph.model[i].set_pressure(P_vector[data_node.index == pipeline[i].input_node] ** 0.5, 
                                        P_vector[data_node.index == pipeline[i].output_node] ** 0.5) 
                idem_diaganal[i, i] = pipeline[i].get_idem()

            # Опеределить ошибку
            mistake = np.abs(A.T @ P_vector - F_vector).max()
            step += 1   
    
    def get_F_vector(self, X_vector: np.array) -> np.array:
        return np.array([arc.model.get_pressure_losses(flow_rate) for arc, flow_rate in zip(self.graph.arcs, X_vector)])
    
    def get_F_diff_inv(self, X_vector: np.array) -> np.array:
        F_diff_inv = np.zeros((self.n, self.n))
        for i in range(self.n):
            F_diff_inv[i,i] = 1 / self.graph.arcs[i].model.get_pressure_derivatives(X_vector[i])
        return F_diff_inv


        
