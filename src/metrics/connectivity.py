import networkx as nx

def largest_component_size(G, weight_threshold=0.0):
    """
    Compute LCC considering only edges above weight_threshold.
    """
    if G.is_directed():
        H = nx.DiGraph(
            (u, v) for u, v, d in G.edges(data=True)
            if d.get("weight", 1.0) > weight_threshold
        )
    else:
        H = nx.Graph(
            (u, v) for u, v, d in G.edges(data=True)
            if d.get("weight", 1.0) > weight_threshold
        )

    if len(H.nodes()) == 0:
        return 0

    components = (
        nx.weakly_connected_components(H)
        if H.is_directed()
        else nx.connected_components(H)
    )

    return max(len(c) for c in components)
