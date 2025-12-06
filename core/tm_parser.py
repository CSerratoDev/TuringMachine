from core.tm_model import MachineConfig, Transition

def parse(filename: str) -> MachineConfig:
    with open(filename, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines() if l.strip() and not l.startswith("#")]

    if len(lines) < 6:
        raise ValueError("Incomplete file, missing headers.")

    states = lines[0].split()
    input_ribbon = list(lines[1].split())
    tape_alphabet = lines[2].split()
    start_state = lines[3]
    final_states = lines[4].split()

    transitions = []
    for i, line in enumerate(lines[5:], start=6):
        parts = line.split()
        if len(parts) != 5:
            raise ValueError(f"Invalid transition at line {i}.")

        t = Transition(*parts)
        transitions.append(t)

    return MachineConfig(
        states=states,
        alphabet=tape_alphabet,
        start_state=start_state,
        final_states=final_states,
        transitions=transitions,
        white_symbol="Δ",
        input_ribbon=input_ribbon
    )

class TuringMachineParser:
    pass