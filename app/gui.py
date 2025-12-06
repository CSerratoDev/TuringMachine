import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from graphviz import Digraph

from core.tm_parser import TuringMachineParser, parse
from core.tm_simulator import TuringMachineSimulator
from render.tape_renderer import TapeRenderer, render

class TuringMachineGUI:
    def __init__(self):
        self.sim = None
        self.tape_renderer = TapeRenderer()

        self.root = tk.Tk()
        self.root.geometry("1000x900")
        self.root.title("System by Turing Machine")
        self.root.resizable(True, True)

        self.upload_btn = ttk.Button(self.root, text="Upload (.txt)", command=self.read_txt)
        self.upload_btn.pack(pady=10)

        self.text = tk.Text(self.root, height=10, wrap="none")
        self.text.pack(fill="x", padx=10, pady=5)

        self.tape_label = tk.Label(self.root)
        self.tape_label.pack(pady=10)

        self.diagram_label = tk.Label(self.root)
        self.diagram_label.pack(pady=10)

        self.button = ttk.Button(self.root, text="Next", command=self.on_step, state="disabled")
        self.button.pack(pady=10)

        self._resample_filter = Image.Resampling.LANCZOS

    def draw(self):
        if not self.sim:
            return

        path = render(self.sim.cfg.input_ribbon if False else self.sim.ribbon, self.sim.head)
        try:
            pil_image = Image.open(path)
            pil_image.thumbnail((900, 200), self._resample_filter)
            img = ImageTk.PhotoImage(pil_image)

            self.tape_label.configure(image=str(img))
            self.tape_label.image = img
        except Exception as e:
            print("Tape draw error:", e)

    def draw_diagram(self, last_transition=None):
        if not self.sim:
            return

        try:
            cfg = self.sim.cfg  # MachineConfig

            g = Digraph("DiagramaMT", format="png")
            g.attr(rankdir='LR', size="8,5", ratio="fill", bgcolor='transparent')

            for state in cfg.states:
                is_current = (state == self.sim.state)
                g.node(
                    state,
                    shape="doublecircle" if state in cfg.final_states else "circle",
                    style="filled",
                    fillcolor="#5DADE2" if is_current else "white",
                    penwidth="3" if is_current else "1",
                )

            edges = {}
            for t in cfg.transitions:
                key = (t.state_from, t.state_to)
                label = f"{t.read}; {t.write}, {t.direction}"
                is_active = (t is last_transition)
                edges.setdefault(key, []).append((label, is_active))

            for (src, dst), label_list in edges.items():
                highlight = any(active for _, active in label_list)
                final_label = "\n".join(f"<{lbl}>" if active else lbl for lbl, active in label_list)

                g.edge(
                    src,
                    dst,
                    label=final_label,
                    color="red" if highlight else "black",
                    penwidth="2.5" if highlight else "1",
                    fontsize="10"
                )

            g.node("start_invisible", shape="point", width="0")
            g.edge("start_invisible", cfg.start_state)

            output = "temp_diagram"
            g.render(output, cleanup=True)
            img_path = output + ".png"

            if os.path.exists(img_path):
                img = Image.open(img_path)
                img.thumbnail((700, 400), self._resample_filter)
                tk_img = ImageTk.PhotoImage(img)

                self.diagram_label.config(image=str(tk_img))
                self.diagram_label.image = tk_img

        except Exception as e:
            print("Diagram error:", e)

    def on_step(self):
        if not self.sim:
            return

        ok, last_transition = self.sim.step_once()

        self.draw()
        self.draw_diagram(last_transition)

        if not ok:
            msg = "ACCEPT" if self.sim.is_accepted() else "REJECT"
            messagebox.showinfo("Resultado", msg)
            self.button.config(state="disabled")

    def read_txt(self):
        file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if not file:
            return

        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, content)

        try:
            TuringMachineParser()
            config = parse(file)
            self.sim = TuringMachineSimulator(config)

            self.button.config(state="normal")
            self.draw()
            self.draw_diagram()

        except Exception as e:
            messagebox.showerror("Parser error", str(e))
            self.sim = None
            self.button.config(state="disabled")

    def run(self):
        self.root.mainloop()
