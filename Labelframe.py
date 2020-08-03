import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Label frame ")

label_frame=ttk.LabelFrame(root,text="Enter your details below")
label_frame.grid(row=0,column=0,padx=100,pady=10)

labels=["Enter your name : ","Enter your age : ","Enter your email : ","Country : ","State : ","City : ","Pinal Code","Mob. No.: "]
for i in range(len(labels)):
    Label="Label" + str(i)
    Label=ttk.Label(label_frame, text=labels[i])
    Label.grid(row=i+1,column=0,sticky=tk.W,padx=10,pady=2)


var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()
var4=tk.StringVar()
var5=tk.StringVar()
var6=tk.StringVar()
var7=tk.StringVar()
var8=tk.StringVar()
variables=[var1,var2,var3,var4,var5,var6,var7,var8]


for i in range(len(labels)):
    entries="Entry" + str(i)
    entries=ttk.Entry(label_frame, width=10,textvariable=variables[i])
    entries.grid(row=i+1,column=1,sticky=tk.W,padx=17,pady=2)

button_label=tk.Button(label_frame,text="Submit")
button_label.grid(row=9,columnspan=2,padx=0,pady=4)

for child in label_frame.winfo_children():
    child.grid_configure(padx=12,pady=2)

root.mainloop()