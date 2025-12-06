from core.tm_model import MachineConfig

class TuringMachineSimulator:

    def __init__(self, config: MachineConfig):
        self.step = None
        self.state = None
        self.head = None
        self.ribbon = None
        self.cfg = config
        self.reset()

    def reset(self):
        self.ribbon = self.cfg.input_ribbon.copy()
        self.head = 0
        self.state = self.cfg.start_state
        self.step = 0

    def step_once(self):
        if self.head < 0:
            self.ribbon.insert(0, self.cfg.white_symbol)
            self.head = 0
        elif self.head >= len(self.ribbon):
            self.ribbon.append(self.cfg.white_symbol)

        current_symbol = self.ribbon[self.head]

        for t in self.cfg.transitions:
            if t.state_from == self.state and t.read == current_symbol:
                self.ribbon[self.head] = t.write
                self.state = t.state_to
                self.head += 1 if t.direction == "R" else -1
                self.step += 1
                return True, t

        return False, None

    def is_accepted(self):
        return self.state in self.cfg.final_states
