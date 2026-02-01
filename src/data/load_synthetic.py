import json

def load_synthetic_ecosystem(path):
    with open(path, "r") as f:
        data = json.load(f)

    species = [n["id"] for n in data["nodes"]]
    edges = [(e["source"], e["target"]) for e in data["edges"]]

    return species, edges
