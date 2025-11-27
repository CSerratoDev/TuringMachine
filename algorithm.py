from graphviz import Digraph

def septuple(filename):
    print(f"Leyendo archivo {filename}...")

    with open(filename, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines()]

    if len(lines) < 5:
        raise ValueError("El archivo no contiene las líneas mínimas necesarias")

    states = lines[0].split()
    input_ribbon = list(lines[1].strip())
    ribbon = lines[2].split()

    start_state_raw = lines[3].strip()
    start_state = start_state_raw.split()[0]

    final_states = lines[4].split()

    transitions = []
    for line in lines[5:]:
        parts = line.split()
        if len(parts) != 5:
            print(f"Advertencia: línea invalida en transición -> {line}")
            continue

        state_actual, symbol, next_state, direction, state_next = parts

        transitions.append(
            (state_actual, symbol, next_state, direction, state_next)
        )

    return {
        "states": states,
        "input_ribbon": input_ribbon,
        "ribbon": ribbon,
        "start_state": start_state,
        "final_states": final_states,
        "transitions": transitions,
    }

def execute_machine(filename):
    ribbon = filename["input_ribbon"].copy()
    head = 0
    state = filename["start_state"]
    white = "Δ"
    transitions = filename["transitions"]
    step = 0

    print(f"Cinta: {ribbon}")

    while True:
        if head < 0:
            ribbon.insert(0, white)
            head = 0
        elif head >= len(ribbon):
            ribbon.append(white)

        current_symbol = ribbon[head]
        print(f"\nCabezal en {head}, Estado {state}, Leyendo {current_symbol}")

        draw_machine(ribbon, head, state, step)
        step += 1

        transition_found = False

        for state_actual, symbol, next_symbol, direction, state_next in transitions:
            if state_actual == state and symbol == current_symbol:
                print(f"Transicion: ({state_actual}, {symbol}) -> ({next_symbol}, {direction}, {state_next})")

                ribbon[head] = next_symbol
                state = state_next
                transition_found = True

                if direction == "R":
                    head += 1
                elif direction == "L":
                    head -= 1

                print("\nCinta", "".join(ribbon))
                break

        if not transition_found:
            print("Maquina terminada y palabra copiada correctamente")
            print("Cinta final:", "".join(ribbon))
            break

def draw_machine(ribbon, head, state, step):
    # Usamos el motor por defecto (dot) que maneja bien jerarquías (arriba/abajo)
    g = Digraph("CintaMT", format="png")

    # Ajustes para que se vea más compacto
    g.attr(nodesep="0.1")  # Espacio horizontal entre nodos
    g.attr(ranksep="0.1")  # Espacio vertical entre capas

    # Nombres de los nodos especiales
    current_cell_node = f"cell_{head}"
    state_node_name = "state_display"
    arrow_node_name = "arrow_display"

    # --- 1. CAPA SUPERIOR: El Estado ---
    # shape="plaintext" hace que no tenga bordes, solo el texto
    g.node(state_node_name, label=state, shape="plaintext", fontcolor="blue", fontsize="16")

    # --- 2. CAPA MEDIA: La Cinta ---
    tape_nodes = []
    for i, symbol in enumerate(ribbon):
        visible = symbol if symbol != " " else "_"
        node_name = f"cell_{i}"

        # Usamos shape="box" para que parezcan celdas de cinta
        # fixedsize=true ayuda a que todas sean del mismo tamaño
        g.node(node_name, label=visible, shape="box", width="0.6", height="0.6", fontsize="14")
        tape_nodes.append(node_name)

    # Subgrafo para forzar que todas las celdas de la cinta estén al mismo nivel horizontal
    with g.subgraph() as s:
        s.attr(rank="same")
        for node in tape_nodes:
            s.node(node)

    # Conectamos las celdas horizontalmente con líneas invisibles para mantener el orden
    for i in range(len(tape_nodes) - 1):
        g.edge(tape_nodes[i], tape_nodes[i + 1], style="invis")

    # --- 3. CAPA INFERIOR: La Flecha ---
    g.node(arrow_node_name, label="↑", shape="plaintext", fontsize="24", fontcolor="red")

    # --- CONEXIONES VERTICALES (El truco de la alineación) ---

    # 1. Conectamos el ESTADO con la CELDA ACTUAL.
    # Una arista invisible (style="invis") fuerza a que el estado esté "arriba" en la jerarquía.
    g.edge(state_node_name, current_cell_node, style="invis")

    # 2. Conectamos la CELDA ACTUAL con la FLECHA.
    # Esto fuerza a que la flecha esté "abajo" en la jerarquía.
    g.edge(current_cell_node, arrow_node_name, style="invis")

    # Guardar la imagen
    filename = f"cinta_paso_{step}"
    g.render(filename, cleanup=True)
    print(f"Image saved {filename}.png")


if __name__ == "__main__":
    mt = septuple("mt.txt")
    execute_machine(mt)