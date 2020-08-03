import tkinter
import tkinter as tk
from tkunter import ttk

root=tk.Tk()
root.title("TabControl")

nb=ttk.Notebook(root)
page1=ttk.Frame(tb)
page2=ttk.Frame(tb)
nb.add(page1,text="First Window")
nb.add(page2,text="Second Window")
#nb.grid(row=0,column=0)
nb.pack(expand=True,fill="both")

label1=ttk.Label(page1,text="Enter your name : ")
label1.grid(row=0,column=0)

entry=ttk.Entry(page1,width=20)
entry.grid(row=0,column=1)

label2=ttk.Label(page2,text="Enter your name : ")
label2.grid(row=0,column=0)

entry=ttk.Entry(page2,width=20)
entry.grid(row=0,column=1)


root.mainloop()