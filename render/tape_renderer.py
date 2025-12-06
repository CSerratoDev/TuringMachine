from graphviz import Digraph

def render(ribbon, head ):
    g = Digraph("Tape", format="png")
    g.attr(bgcolor='transparent', rankdir="LR", nodesep="0.3")

    tape_nodes = []

    for i, symbol in enumerate(ribbon):

        color = "yellow" if i == head else "white"
        node_name = f"cell_{i}"

        g.node(
            node_name,
            label=symbol,
            shape="box",
            style="filled",
            fillcolor=color,
            width="0.5",
            height="0.5"
        )

        tape_nodes.append(node_name)

    for i in range(len(tape_nodes) - 1):
        g.edge(tape_nodes[i], tape_nodes[i + 1], style="invis")

    path = "temp_tape"
    g.render(path, cleanup=True)

    return path + ".png"


class TapeRenderer:
    pass