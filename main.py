import tkinter as tk
from tkinter import messagebox, filedialog

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
def read_txt():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "r") as f:
            content = f.read()
        text.delete(1.0, tk.END)
        text.insert(tk.INSERT, content)

    button_status()

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
button = tk.Button(root, text="Create", cursor="hand2", state="disabled")
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