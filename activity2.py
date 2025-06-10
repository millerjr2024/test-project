import tkinter as tk

def update_label(event):
    text = entry.get()
    label.config(text=text)

root = tk.Tk()
root.title("Simple App")

entry = tk.Entry(root)
entry.pack()
entry.bind("<KeyRelease>", update_label)  

label = tk.Label(root, text="")
label.pack()

root.mainloop()

