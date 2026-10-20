import numpy as np
import networkx as nx


def gabriel_graph(points, y=None):
    """Return the Gabriel graph as a NetworkX graph.

    Nodes are point indices. Each edge's ``weight`` is the Euclidean
    distance between its endpoints.
    """
    points = np.asarray(
        points if y is None else np.column_stack((points, y)),
        dtype=float,
    )

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("points must have shape (n, 2)")
    if not np.isfinite(points).all():
        raise ValueError("points must contain only finite values")
    if len(np.unique(points, axis=0)) != len(points):
        raise ValueError("points must not contain duplicates")

    n = len(points)
    scale = max(1.0, np.ptp(points, axis=0).max()) if n else 1.0
    tol = 16 * np.finfo(float).eps * scale**2

    graph = nx.Graph()
    graph.add_nodes_from(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            others = np.concatenate((points[:i], points[i + 1:j], points[j + 1:]))
            if len(others) and np.any(
                np.sum((others - points[i]) * (others - points[j]), axis=1) < -tol
            ):
                continue

            distance = float(np.linalg.norm(points[i] - points[j]))
            graph.add_edge(i, j, weight=distance)

    return graph



def gen_random_path(graph, path_length):
    """Generate a random path of given length in the graph."""
    if path_length < 1:
        raise ValueError("path_length must be at least 1")
    if len(graph) == 0:
        raise ValueError("graph must not be empty")

    start_node = np.random.choice(graph.nodes)
    path = [start_node]

    while len(path) < path_length:
        neighbors = list(graph.neighbors(path[-1]))
        if not neighbors:
            break
        next_node = np.random.choice(neighbors)
        path.append(next_node)

    return path