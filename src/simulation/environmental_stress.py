def apply_environmental_stress(G, stress_level):
    """
    Apply environmental stress by weakening all interactions.

    stress_level: float in [0, 1]
        0.0 = no stress
        1.0 = complete interaction loss
    """
    G_stressed = G.copy()

    for u, v in G_stressed.edges():
        G_stressed[u][v]["weight"] = max(0.0, 1.0 - stress_level)

    return G_stressed
