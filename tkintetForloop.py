import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Loop")

#page_label=ttk.Label(root, text="Login Page")
#page_label.pack()

#name_label=ttk.Label(root, text="Enter your name : ")
#name_label.grid(row=0, column=0,sticky=tk.W)
labels=["Enter your name : ","Enter your age : ","Enter your email : ","Country : ","State : ","City : "]
for i in range(len(labels)):
    Labeled="Label" + str(i)
    Labeled=ttk.Label(root, text=labels[i])
    Labeled.grid(row=i,column=0,sticky=tk.W)




root.mainloop()