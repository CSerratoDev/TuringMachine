import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("900x800")
root.title("System by Turing Machine")

def input_text():
    messagebox.showinfo("Accepting Chain", "creating turing machine with live model")

button = tk.Button(root, text="Create", command=input_text)
button.pack()

label = tk.Label(root, text= "created by csrratodev")
label.pack()

root.mainloop()