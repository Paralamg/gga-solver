from graphs.graph import Graph
from models.pipe import Pipe
from graphs.graph_node import Node

def create_graph_with_three_pipes() -> Graph:
    graph = Graph()

    supplier = Node(0, 'pressure', pressure=5e6)
    consumer_1 = Node(2, 'pressure', pressure=2e6)
    consumer_2 = Node(3, 'pressure', pressure=2.2e6)
    node = Node(1)

    graph.add_node(supplier)
    graph.add_node(consumer_1)
    graph.add_node(consumer_2)
    graph.add_node(node)
    
    pipe_1 = Pipe(0, 40e3, 1.22, 0.003)
    pipe_2 = Pipe(1, 40e3, 1.22, 0.003)
    pipe_3 = Pipe(2, 40e3, 1.22, 0.003)

    graph.add_arc(supplier, node, pipe_1)
    graph.add_arc(consumer_1, node, pipe_2)
    graph.add_arc(node, consumer_2, pipe_3)

    return graph

def create_graph_contest() -> Graph:
    graph = Graph()

    nodes = [Node(0, 'pressure', pressure=5e6)]
    for i in range(1, 5):
        nodes.append(Node(i))
    nodes.append(Node(5, 'pressure', pressure=2e6))
    nodes.append(Node(6, 'pressure', pressure=2.2e6))

    for node in nodes:
        graph.add_node(node)

    pipeline = [
        Pipe(0, 40e3, 1.22, 0.003),
        Pipe(1, 40e3, 1.22, 0.003),
        Pipe(2, 40e3, 1.22, 0.003),
        Pipe(3, 40e3, 1.22, 0.003),
        Pipe(4, 40e3, 1.22, 0.003),
        Pipe(5, 40e3, 1.22, 0.003),
        Pipe(6, 40e3, 1.22, 0.003),
        Pipe(7, 40e3, 1.22, 0.003),
        Pipe(8, 40e3, 1.22, 0.003)]

    graph.add_arc(nodes[0], nodes[1], pipeline[0])
    graph.add_arc(nodes[1], nodes[2], pipeline[1])
    graph.add_arc(nodes[2], nodes[3], pipeline[2])
    graph.add_arc(nodes[4], nodes[1], pipeline[3])
    graph.add_arc(nodes[3], nodes[4], pipeline[4])
    graph.add_arc(nodes[1], nodes[3], pipeline[5])
    graph.add_arc(nodes[2], nodes[4], pipeline[6]) 
    graph.add_arc(nodes[4], nodes[6], pipeline[7])
    graph.add_arc(nodes[2], nodes[5], pipeline[8])

    return graph




