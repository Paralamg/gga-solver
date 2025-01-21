class Node:
    def __init__(self, id: int, sign='flow', flow_rate=0., pressure=0.):
        self.sign = sign
        self.neighbors = []
        self.pressure = 0.
        self.temperature = 0.
        self.flow_rate = 0.
        self.pressure_calculated = 0.
        self.temperature_calculated = 0.
        self.flow_rate_calculated = 0.
        self.model = None
        self.id = id

    def __repr__(self):
        return f"Node('{self.sign}')"

    def get_arcs_in(self):
        pass

    def get_arcs_out(self):
        pass
