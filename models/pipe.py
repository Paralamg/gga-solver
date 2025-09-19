import math
class Pipe:
    def __init__(self, id: int, length: float, diameter: float, roughness: float):
        # Получить исходные данные для расчёта
        self.l = length
        self.d = diameter
        self.k = roughness
        self.id = id
        self.mu = 17.5
        self.t = 290
        self.p_sto = 101325
        self.t_crit = 200
        self.p_crit = 4.75 * 10 ** 6

        # Рассчитать постоянные значения
        self.gas_const = 8314 / self.mu
        self.t_pr = self.t / self.t_crit
        self.p_pr = self.p_sto / self.p_crit
        self.lamb = 0.067 * (2 * self.k / self.d) ** 0.2

    def get_pressure_losses(self, flow_rate: float, inlet_pressure: float, outlet_pressure: float):
        """
        Находит значение функции F(x) для конкретной модели

        :param flow_rate: расход
        :param inlet_pressure: давление на входе
        :param outlet_pressure: давление на выходе
        :return: значение функции F(x)
        """
        self.set_pressure(inlet_pressure, outlet_pressure)
        idem = self.get_idem()
        return idem * flow_rate * abs(flow_rate)

    def get_pressure_derivatives(self, flow_rate: float, inlet_pressure: float, outlet_pressure: float):
        """
        Находит значение производной функции F'(x) для конкретной модели

        :param flow_rate: расход
        :param inlet_pressure: давление на входе
        :param outlet_pressure: давление на выходе
        :return:
        """
        self.set_pressure(inlet_pressure, outlet_pressure)
        idem = self.get_idem()
        return 2 * idem * abs(flow_rate)


    def get_idem(self):
        """
        Возвращает постоянную часть для расчёта потенциала
        """
        return 16 * self.lamb * self.get_z_sto() * self.gas_const * self.t * self.l / (math.pi ** 2 * self.d ** 5)

    def set_pressure(self, inlet_pressure: float, outlet_pressure: float):
        """
        Находит среднее значение давления на участке трубопровода по формуле приведённой в СТО Газпром 202-3.5-051-2006
        inlet_pressure - давление на входе
        outlet_pressure - давление на выходе
        """
        self.p_sto = 2 / 3 * (inlet_pressure + outlet_pressure ** 2 / (inlet_pressure + outlet_pressure))
        self.p_pr = self.p_sto / self.p_crit

    def get_z_sto(self):
        """
        Возвращает значение коэффициента сжатия по формуле приведённой в СТО Газпром 202-3.5-051-2006
        """
        self.z_A1 = -0.39 + 2.03 / self.t_pr - 3.16 / self.t_pr ** 2 + 1.09 / self.t_pr ** 3
        self.z_A2 = 0.0423 - 0.1812 / self.t_pr + 0.2124 / self.t_pr ** 2
        self.z_sto = 1 + self.z_A1 * self.p_pr + self.z_A2 * self.p_pr ** 2
        return self.z_sto