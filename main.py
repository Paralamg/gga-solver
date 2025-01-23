import factories.graph_factory as graph_factory
from solvers.gga_solver import GgaSolver
from graphs.graph import Graph

def main():
    graph = graph_factory.create_graph_with_three_pipes()
    solver = GgaSolver()
    solver.solve(graph)
    print_result(graph)

def print_result(graph: Graph):
    print(f'Graph with {graph.get_m()} nodes and {graph.get_n()} arcs')
    print()
    print(f'Nodes:')
    print(f'{'Id':>3}\t{'Sign':8}\t{'Flow_rate':>15}\t{'Pressure':>14}')
    for node in sorted(graph.nodes, key=lambda x: x.id):
        print(node)
    print()
    print(f'Arcs:')
    print(f'{"Id":>3}\t{"Start":>3} -> {"End":<3}\t{"Flow_rate":>15}\t{"Inlet_pressure":>14} -> {"Outlet_pressure":>14}')
    for arc in sorted(graph.arcs, key=lambda x: x.id):
        print(arc)

if __name__ == '__main__':
    main()