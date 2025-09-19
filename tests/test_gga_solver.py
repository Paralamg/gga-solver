from unittest import TestCase
import factories.graph_factory as graph_factory
from solvers.gga_solver import GgaSolver

class TestGGASolver(TestCase):
    def test_solve(self):
        graph = graph_factory.create_graph_with_three_pipes()
        solver = GgaSolver()
        solver.solve(graph)
        self.assertTrue(graph.is_normal_result)

