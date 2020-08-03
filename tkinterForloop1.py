import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Loop")

#page_label=ttk.Label(root, text="Login Page")
#page_label.pack()

#name_label=ttk.Label(root, text="Enter your name : ")
#name_label.grid(row=0, column=0,sticky=tk.W)
labels=["Enter your name : ","Enter your age : ","Enter your email : ","Country : ","State : ","City : "]

vars=["Name","Age","Email","Country","State","City"]

for i in range(len(labels)):
    Labeled="Label" + str(i)
    Labeled=ttk.Label(root, text=labels[i])
    Labeled.grid(row=i,column=0,sticky=tk.W,padx=17,pady=2)

#for i in range(len(labels)):
#    variable="var"+str(i)
#    variable=tk.StringVar()
var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()
var4=tk.StringVar()
var5=tk.StringVar()
var6=tk.StringVar()
variables=[var1,var2,var3,var4,var5,var6]


for i in range(len(labels)):
    entries="Entry" + str(i)
    entries=ttk.Entry(root, width=10,textvariable=variables[i])
    entries.grid(row=i,column=1,sticky=tk.W,padx=17,pady=2)

def action():
    for i in range(len(labels)):
        varlabel=ttk.Label(root,text=variables[i].get())
        varlabel.grid(row=i+7,columnspan=3)
        
        
    

button_label=tk.Button(root,text="Submit",command=action)
button_label.grid(row=6,columnspan=3)

root.mainloop()