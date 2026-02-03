import networkx as nx

def build_ecological_layer(species, interactions):
    G = nx.DiGraph()
    G.add_nodes_from(species)
    G.add_edges_from(interactions)
    return G
