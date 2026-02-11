import numpy as np
from copy import deepcopy
from src.metrics.connectivity import largest_component_size

def robustness_curve(G, removal_order, steps=None):
    if steps is None:
        steps = len(G.nodes())


    G_work = deepcopy(G)
    N0 = len(G.nodes())


    fractions = []
    lcc_sizes = []


    for i in range(steps + 1):
        fractions.append(i / N0)
        if len(G_work.nodes()) > 0:
            lcc_sizes.append(largest_component_size(G_work) / N0)
        else:
            lcc_sizes.append(0)


        if i < steps and i < len(removal_order):
            G_work.remove_node(removal_order[i])


    return np.array(fractions), np.array(lcc_sizes)