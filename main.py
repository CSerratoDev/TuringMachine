import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os
from algorithm import septuple, execute_machine


root = tk.Tk()
root.geometry("900x800")
root.title("System by Turing Machine")

ribbon_aux = tk.StringVar()

def message_create():
    messagebox.showinfo("Accepting Chain", "creating turing machine with live model")

#Functions Input text by user
def button_status():
    if ribbon_aux.get().strip() or text.get("1.0", tk.END).strip():
        button.config(state="normal")
    else:
        button.config(state="disabled")
'''
def input_text():
    alphabet = str(input_ribbon.get())
    label_result.config(text="Your final answer is: " + str(alphabet))
'''

def drawing_images():
    for widget in root.pack_slaves():
        if isinstance(widget, tk.Label) and hasattr(widget, "image"):
            widget.destroy()

    frame_images = tk.Frame(root)
    frame_images.pack(pady=10)

    carpet = "."
    images = [f for f in os.listdir(carpet) if f.startswith("cinta_paso_") and f.endswith(".png")]

    for image_name in sorted(images):
        route = os.path.join(carpet, image_name)
        img = Image.open(route)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)

        lbl = tk.Label(frame_images)
        lbl.image = img_tk
        lbl.pack(pady=5)

def read_txt():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "r") as f:
            content = f.read()
        text.delete(1.0, tk.END)
        text.insert(tk.INSERT, content)

    button_status()
    mt = septuple(file)
    execute_machine(mt)
    drawing_images()

#Input
'''
label_ribbon = tk.Label(text="Enter an alphabet for the machine", font=("Arial", 12, "bold"), pady=10)
input_ribbon = tk.Entry(root, textvariable=ribbon_aux)
label_ribbon.pack()
input_ribbon.pack()
'''
label_result = tk.Label(text="Your final answer will be here!", font=("Arial", 12, "underline"), fg="green", pady=5)
label_result.pack()

#Create button
button = tk.Button(root, text="Create", command=message_create, cursor="hand2", state="disabled")
button.pack()

#Upload button
upload_button = tk.Button(root, text="Upload file", command=read_txt, cursor="hand2")
upload_button.pack()

text = tk.Text(root)
text.pack(expand=True)

#Exit button
exit_button = tk.Button(root, text="Quit", command=root.destroy, cursor="hand2")
exit_button.pack()

#Copyright
label = tk.Label(root, text= "created by csrratodev")
label.pack()

root.mainloop()