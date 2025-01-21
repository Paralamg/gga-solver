import pandas as pd
import numpy as np
import math
from numpy import NaN as _

class Pipe:   
    def __init__(self, input_node, output_node, length, diameter, roughness, molal_mass, temperature, T_crit, P_crit):
        # Получить исходые данные для расчёта 
        self.l = length
        self.d = diameter
        self.mu = molal_mass
        self.k = roughness
        self.t = temperature
        self.input_node = input_node
        self.output_node = output_node
        self.p_sto = 101325
        self.t_crit = T_crit
        self.p_crit = P_crit
        
        # Расчитать постоянные заначения 
        self.gas_const = 8314 / self.mu
        self.t_pr = self.t / self.t_crit
        self.p_pr = self.p_sto / self.p_crit
        self.lamb = 0.067 * (2 * self.k / self.d) ** 0.2

    def get_idem(self):
        '''
        Возвращает постоянную часть для расчёта потенциала
        '''
        return 16 * self.lamb * self.get_z_sto() * self.gas_const * self.t * self.l / (math.pi ** 2 * self.d ** 5)
    
    def set_pressure(self, h_pressure, l_pressure):
        '''
        Находит среднее значение давления на учатске трубопровода по формуле приведённой в СТО Газпром 202-3.5-051-2006
        h_pressure - давление на входе
        l_pressure - давление на выходе
        '''
        self.p_sto = 2 / 3 * (h_pressure + l_pressure ** 2 / (h_pressure + l_pressure))
        self.p_pr = self.p_sto / self.p_crit
      
    def get_z_sto(self):
        '''
        Возвращает значение коэффициента сжания по формуле приведённой в СТО Газпром 202-3.5-051-2006
        '''
        self.z_A1 = -0.39 + 2.03 / self.t_pr - 3.16 / self.t_pr ** 2 + 1.09 / self.t_pr ** 3
        self.z_A2 = 0.0423 - 0.1812 / self.t_pr + 0.2124 / self.t_pr ** 2 
        self.z_sto = 1 + self.z_A1 * self.p_pr + self.z_A2 * self.p_pr ** 2
        return self.z_sto

              
# Исходные данные
LENGTHES = np.array([1, 1, 0.2, 1.5, 0.7, 2, 0.9, 0.1, 0.5, 0.2,
                         0.2, 1, 0.2, 1, 0.4, 0.3, 1.8, 0.6, 1.3, 0.5,
                         0.2, 0.2, 1.7, 0.3, 0.9, 1, 0.4, 1, 0.7, 0.6,
                         0.8]) * 10 ** 3  # метры
DIAMETRES = (0.7, 0.7, 0.2, 0.7, 0.7, 0.7, 0.7, 0.7, 0.5, 0.5,
             0.5, 0.7, 0.2, 0.7, 0.2, 0.7, 0.7, 0.7, 0.7, 0.5,
             0.5, 0.5, 0.7, 0.3, 0.7, 0.7, 0.3, 0.7, 0.7, 0.3,
             0.7)  # метры
WAYS = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [4, 6], [5, 7], [6, 7], [7, 8], [8, 9],
        [8, 10], [5, 11], [11, 12], [11, 13], [13, 14], [13, 15], [6, 15], [15, 16], [16, 17], [17, 18],
        [18, 19], [18, 20], [17, 21], [21, 22], [21,25], [16, 23], [23, 24], [23, 25], [25, 26], [26, 27],
        [26, 1]]
INPUT_NODES = [0, 1, 2, 2, 4, 4, 5, 6, 7, 8, 8, 5, 11, 11, 13, 13, 6, 15, 16, 17, 18, 18, 17, 21, 21, 16, 23, 23, 25, 26, 26]
OUTPUT_NODES = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 25, 23, 24, 25, 26, 27, 1]
PRESSURE = np.array([0.3, _, _, 0.1, _, _, _, _, _, 0.1, 0.1,
                     _, 0.1, _, 0.1, _, _, _, _, 0.1, 0.1,
                     _, 0.1, _, 0.1, _, _, 0.1]) * 10 ** 6  # Па
Q = np.array([_, 0, 0, _, 0, 0, 0, 0, 0, _, _,
              0, _, 0, _, 0, 0, 0, 0, _, _,
              0, _, 0, _, 0, 0, _])

# Характеристика газа 
roughness = 0.05 / 10 ** 3
temperature = 290
molal_mass = 17.5
T_crit = 200
P_crit = 4.75 * 10 ** 6

# Точность расчёта
ACCURACY = 0.001

# Создадим таблицу с данными для вершин
data_edge = pd.DataFrame({'input_nodes': INPUT_NODES,
                          'output_nodes': OUTPUT_NODES,
                          'lengthes': LENGTHES,
                          'diametres': DIAMETRES,
                          'roughness': roughness,
                          'temperature': temperature})


# Создадим таблицу с данными для рёбер
data_node = pd.DataFrame({'pressure': PRESSURE,
                          'Q':Q})
data_node.sort_values('Q', inplace=True) # сортировка на Q1 и P2

# Найдем количество известных притоков/оттоков по узлам (k), количество узлов (m) и рёбер (n)
k = data_node['Q'].notna().sum() #  Ставит True, если Q не NaN, и суммириет количество True
m = len(data_node['Q']) # Длина столбца Q
n = len(data_edge['diametres']) # Длина столбца diametres

print(f'k = {k}', f'm = {m}', f'n = {n}', sep='\n')
data_node.fillna(data_node.mean(), inplace=True)

# Зададим вектор давлений в квадрате и расходов
P_vector = np.array(data_node['pressure']) ** 2
Q_vector = np.array(data_node['Q'])

# Создадим матрицу инцидентности А, А1, А2 (Аналог)
A = np.zeros((m, n))
for num, way in enumerate(data_edge[['input_nodes', 'output_nodes']].values):
    A[way[0], num] = 1
    A[way[1], num] = -1
A = A[data_node.index] # Сортировка по индексам
A1 = A[:k] # Взять первые k строк матрицы A
A2 = A[k:m] # Взять строки матрицы A с k до m (k включительно, m не включительно)

# Создать экземпляры трубопровода для трубопроводной сети
pipeline = [Pipe(input_node, output_node, length, diameter, roughness, molal_mass, temperature, T_crit, P_crit) 
            for input_node, output_node, length, diameter, roughness, temperature in data_edge.values]

# Создать вектор расходов, диагональную матрицу расходов и матрицу коэффициентов idem
idem_diaganal = np.zeros((n, n))
X_vector = np.random.rand(n)
X_diaganal = np.zeros((n, n))
for i in range(n):
    idem_diaganal[i, i] = pipeline[i].get_idem()
    X_diaganal[i, i] = abs(X_vector[i])

mistake = 1
step = 0
# Цикл до тех пор пока величина ошибки будет больше допустимой
while mistake > ACCURACY and step < 100:
    # Найти F(x), F`(x) и матрицу Максвела в соответсвии с формулами 
    F_vector = idem_diaganal @ X_diaganal @ X_vector
    F_diff = idem_diaganal @ X_diaganal * 2
    F_diff_inv = np.linalg.inv(F_diff)
    maxvel = A1 @ F_diff_inv @ A1.T # (m-k)x(m-k)
    
    # Сделать шаг итераци в соответсвии с выведенными формулами. Получить вектор давлений и расходов по ребрам
    P_vector[:k] = np.linalg.inv(maxvel) @ (Q_vector[:k] - A1 @ X_vector - A1 @ F_diff_inv @ (A2.T @ P_vector[k:] - F_vector))
    X_vector = X_vector + F_diff_inv @ (A.T @ P_vector - F_vector)

    # Обновить диагональную матрицу расходов и матрицу коэффициентов idem, перед которой обновим давления на гранях
    for i in range(n):
        X_diaganal[i, i] = abs(X_vector[i])
        # Обновление давления в соответсвии с номером узла, который соответсвует индексу data_node
        pipeline[i].set_pressure(P_vector[data_node.index == pipeline[i].input_node] ** 0.5, 
                                 P_vector[data_node.index == pipeline[i].output_node] ** 0.5) 
        idem_diaganal[i, i] = pipeline[i].get_idem()

    # Опеределить ошибку
    mistake = np.abs(A.T @ P_vector - F_vector).max()
    step += 1
else:
    print(step)

# Изменить направление движения в гранях, где отрицательный расход, и вывести результат
data_edge.loc[X_vector < 0, 'input_nodes'], data_edge.loc[X_vector < 0, 'output_nodes'] = data_edge.loc[X_vector < 0, 'output_nodes'], data_edge.loc[X_vector < 0, 'input_nodes']
data_edge['X'] = abs(X_vector)
print('Результат по ребрам:')
print(data_edge)


# Давление и расход по узлам
data_node['pressure'] = P_vector ** 0.5 / 10 ** 6
data_node['Q'] = A @ X_vector
data_node.sort_index(inplace=True)
data_node.loc[data_node['Q'].abs() < 10 ** -6, 'Q'] = 0
print('Результат по узлам:')
print(data_node)

