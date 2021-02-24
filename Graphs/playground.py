graph = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"],
         "f": []
         }

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges


