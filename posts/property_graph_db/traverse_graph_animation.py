import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def main():
    fig, ax = plt.subplots()

    G = nx.read_adjlist("student_graph.adj", create_using=nx.DiGraph)
    pos = nx.planar_layout(G)  # positions for all nodes

    nx.draw(G, ax=ax, pos=pos, node_color=['green' for _ in enumerate(G.nodes)], with_labels=True)

    def update(edge: tuple[str, str]):
            # for each frame color different edges

            start, end = edge

            node_color = []
            for node in G.nodes:
                if node == start:
                    node_color.append('blue')
                elif node == end:
                    node_color.append('red')
                else:
                    node_color.append('green')

            nx.draw(G, ax=ax, pos=pos, node_color=node_color, with_labels=True)
            return ax

    ani = FuncAnimation(fig=fig, func=update, frames=nx.dfs_edges(G, source="Alice"), interval=500)
    ani.save(filename="student_graph_traversal.gif", writer="pillow")
    plt.show()


if __name__ == "__main__":
    main()
