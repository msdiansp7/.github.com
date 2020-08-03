import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
import os

root=tk.Tk()

root.title("Message Box")

#labelframe

label_frame=ttk.LabelFrame(root,text="Login")
label_frame.grid(row=0,column=0,padx=60,pady=50)

#Frames
#label_frame=ttk.Frame(label_frame,text="Tab 1")
#label_frame.pack(expand=True,fill="both")
#Tab2=ttk.Frame(label_frame,text="Tab 2")
#Tab2.pack(expand=True,fill="both")


#labels

label1=ttk.Label(label_frame,text="Username : ",font=("Helvetica",10,"bold"))
label1.grid(row=0,column=0,pady=20,sticky=tk.W)

label2=ttk.Label(label_frame,text="Password : ",font=("Helvetica",10,"bold"))
label2.grid(row=0,column=1,pady=20,sticky=tk.W)

#variables

name_var=tk.StringVar()
pass_var=tk.StringVar()

#entrybox

entry1=ttk.Entry(label_frame,width=15,textvariable=name_var)
entry1.grid(row=1,column=0,padx=5,pady=10)

entry2=ttk.Entry(label_frame,width=15,textvariable=pass_var)
entry2.grid(row=1,column=1,padx=5,pady=10)

def submit():
    name=name_var.get()
    password=pass_var.get()
    if name=="" or password=="":
        m_box.showerror("Error","Please enter something !!")
    else:
        m_box.showinfo("Login failed","Wrong Username and password !!")
#    m_box.showinfo("Done","You have successfully signed in")
#    m_box.showerror("Error","Please enter something !!")
#    m_box.showwarning("Warning","You have not enter anything")


button=tk.Button(label_frame,text="Submit",command=submit)
button.grid(row=2,columnspan=2,padx=100,pady=10)
root.mainloop()