class Arc:
    def __init__(self, start, end, model):
        self.start_node = start
        self.end_node = end
        self.model = model
        self.id = model.id