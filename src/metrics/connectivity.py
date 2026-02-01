import networkx as nx

def largest_component_size(G):
    if G.is_directed():
        components = nx.weakly_connected_components(G)
    else:
        components = nx.connected_components(G)
    return max(len(c) for c in components)
