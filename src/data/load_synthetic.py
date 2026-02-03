import json
from pathlib import Path

def load_synthetic_ecosystem(relative_path):
    # Resolve project root (2 levels up from this file)
    project_root = Path(__file__).resolve().parents[2]

    file_path = project_root / relative_path

    with open(file_path, "r") as f:
        data = json.load(f)

    species = [n["id"] for n in data["nodes"]]
    edges = [(e["source"], e["target"]) for e in data["edges"]]

    return species, edges
