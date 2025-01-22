class Arc:
    def __init__(self, start, end, model):
        self.start_node = start
        self.end_node = end
        self.model = model
        self.id = model.id
        self.flow_rate_calculated = 0

    def get_pressure_losses(self, flow_rate: float):
        """
        Находит значение функции F(x) для дуги
        :param flow_rate: расход на дуге
        :return: значение функции F(x)
        """
        return self.model.get_pressure_losses(flow_rate, self.start_node.pressure, self.end_node.pressure)

    def get_pressure_derivatives(self, flow_rate: float):
        """
        Находит значение производной функции F'(x) для дуги
        :param flow_rate: расход на дуге
        :return: значение производной функции F'(x)
        """
        return self.model.get_pressure_derivatives(flow_rate, self.start_node.pressure, self.end_node.pressure)

