import tkinter
import tkinter as tk
from tkinter import ttk

root=tk.Tk()

def func():
    label1=ttk.Label(root,text="Enter your name : ")
    label1.pack(expand=True,fill="y")
    label1.configure (background="#a1abc9")
    
def function():
    pass
#    label1.grid(row=0,column=0)

#menubar=tk.Menu(root)

#menubar.add_command(label="Save",command=func)
#menubar.add_command(label="Save as",command=func)
#menubar.add_command(label="Open",command=func)
#menubar.add_command(label="Copy",command=func)
#menubar.add_command(label="Paste",command=func)

#menu

main_menu=tk.Menu(root)
file_menu=tk.Menu(main_menu)
file_menu.add_command(label="Save",command=func)
#file_menu.add_separator()
file_menu.add_command(label="Save as",command=func)
file_menu.add_command(label="Open",command=func)
file_menu.add_command(label="Copy",command=func)
file_menu.add_command(label="Paste",command=func)

edit_menu=tk.Menu(main_menu)
edit_menu.add_command(label="Open in new window",command=func)


#sub menu

new_menu=tk.Menu(edit_menu)
new_menu.add_command(label="Paint",command=func)
new_menu.add_command(label="Word excel",command=func)
new_menu.add_command(label="Notepad",command=func)


edit_menu.add_cascade(label="Open with",menu=new_menu)
main_menu.add_cascade(label="File",menu=file_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)

root.config(menu=main_menu)






root.mainloop()