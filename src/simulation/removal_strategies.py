import networkx as nx
import random

def random_removal_order(G, seed=None):
    rng = random.Random(seed)
    nodes = list(G.nodes())
    rng.shuffle(nodes)
    return nodes

def targeted_removal_order(G):
    degrees = dict(G.degree())
    return sorted(degrees, key=degrees.get, reverse=True)