class Node:
    def __init__(self, id: int, sign='flow', flow_rate=0., pressure=0.):
        self.sign = sign
        self.neighbors = []
        self.pressure = pressure
        self.flow_rate = flow_rate
        self.pressure_calculated = pressure if sign == 'pressure' else 0.
        self.flow_rate_calculated = flow_rate if sign == 'flow' else 0.
        self.id = id

    def __repr__(self):
        return f"Node('{self.sign}')"
