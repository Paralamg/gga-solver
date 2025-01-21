import unittest
import factories.graph_factory as graph_factory

class  GraphTest(unittest.TestCase):
    
    def test_get_incidence_matrix(self):
        graph = graph_factory.create_graph_with_three_pipes()
        result = graph.get_incidence_matrix()
        self.assertEqual(result.shape, (4, 3))

if __name__ == '__main__':
    unittest.main()