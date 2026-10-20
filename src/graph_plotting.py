import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(graph, x, y):
    fig, ax = plt.subplots(figsize=(10, 10))

    for i, j in graph.edges:
        ax.plot(
            [x[i], x[j]],
            [y[i], y[j]],
            color="black",
            linewidth=0.5,
            alpha=0.5,
        )

    ax.scatter(x, y, s=5)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    return fig, ax


def plot_path(ax, path, x, y, color="red"):
    for i in range(len(path) - 1):
        ax.plot(
            [x[path[i]], x[path[i + 1]]],
            [y[path[i]], y[path[i + 1]]],
            color=color,
            linewidth=2,
            alpha=0.8,
        )
    
    return ax