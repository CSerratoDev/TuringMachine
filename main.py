import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()
root.geometry("900x800")
root.title("System by Turing Machine")

def message_create():
    messagebox.showinfo("Accepting Chain", "creating turing machine with live model")

#Function Input text by user
def input_text():
    alphabet = str(input_ribbon.get())
    label_result.config(text="Your final answer is: " + str(alphabet))

def read_txt():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "r") as f:
            content = f.read()
        text.delete(1.0, tk.END)
        text.insert(tk.INSERT, content)

#Input
label_ribbon = tk.Label(text="Enter an alphabet for the machine")
input_ribbon = tk.Entry()
label_ribbon.pack()
input_ribbon.pack()

label_result = tk.Label(text="Your final answer will be here!")
label_result.pack()

#Create button
button = tk.Button(root, text="Create", command=input_text)
button.pack()

#Upload button
upload_button = tk.Button(root, text="Upload file", command=read_txt)
upload_button.pack()

text = tk.Text(root)
text.pack(expand=True)

#Exit button
exit_button = tk.Button(root, text="Quit", command=root.destroy)
exit_button.pack()

#Copyright
label = tk.Label(root, text= "created by csrratodev")
label.pack()

root.mainloop()