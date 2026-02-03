def remove_species(G, species_to_remove):
    G_shocked = G.copy()
    G_shocked.remove_nodes_from(species_to_remove)
    return G_shocked
