import math
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

    def get_pressure_losses(self, flow_rate: float):
        idem = self.get_idem()
        return idem * flow_rate * abs(flow_rate)

    def get_pressure_derivatives(self, flow_rate: float):
        idem = self.get_idem()
        return 2 * idem * abs(flow_rate)


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