import tkinter as tk

def add():
    try:
        result = int(entry1.get()) + int(entry2.get())
        label_result.config(text="Result: " + str(result))
    except:
        label_result.config(text="Error")

root = tk.Tk()  
root.title("Calculator")  
root.geometry("400x300")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="Add", command=add)
button.pack()

label_result = tk.Label(root, text="Result")
label_result.pack()

root.mainloop()