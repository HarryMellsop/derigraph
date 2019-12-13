import networkx as nx

# Provides an implementation of the underlying equation graph that derigraph utilises for expression
# evaluation and equation atomicity
class EquationGraph(nx.Graph):

    def __init__(self):
        self.G = nx.Graph()
        print("EquationGraph successfully instantiated")
        