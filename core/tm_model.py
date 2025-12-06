from dataclasses import dataclass
from typing import List

@dataclass
class Transition:
    state_from: str
    read: str
    write: str
    direction: str
    state_to: str

@dataclass
class MachineConfig:
    states: List[str]
    alphabet: List[str]
    start_state: str
    final_states: List[str]
    transitions: List[Transition]
    white_symbol: str
    input_ribbon: List[str]