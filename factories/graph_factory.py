from graphs.graph import Graph
from models.pipe import Pipe
from graphs.graph_node import Node

def create_graph_with_three_pipes() -> Graph:
    graph = Graph()

    supplier = Node(0, 'pressure', pressure=5e6)
    consumer_1 = Node(2, 'pressure', pressure=3e6)
    consumer_2 = Node(3, 'pressure', pressure=3e6)
    node =  Node(1)

    graph.add_node(supplier)
    graph.add_node(consumer_1)
    graph.add_node(consumer_2)
    graph.add_node(node)
    
    pipe_1 = Pipe(0, 40e3, 1.22, 0.003)
    pipe_2 = Pipe(0, 40e3, 1.22, 0.003)
    pipe_3 = Pipe(0, 40e3, 1.22, 0.003)

    graph.add_arc(supplier, node, pipe_1)
    graph.add_arc(node, consumer_1, pipe_2)
    graph.add_arc(node, consumer_2, pipe_3)

    return graph




