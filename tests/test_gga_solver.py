from unittest import TestCase
import factories.graph_factory as graph_factory
from solvers.gga_solver import GGASolver
from graphs.graph import Graph


class TestGGASolver(TestCase):
    def test_solve(self):
        graph = graph_factory.create_graph_with_three_pipes()
        solver = GGASolver()
        solver.solve(graph)
        self.assertTrue(graph.is_normal_result)

