import tkinter as tk
from tkinter import ttk
from csv import DictReader,DictWriter
#from tkinter import *
root =tk.Tk()
#root=Tk()
root.title("TkinterGUI")
#ttk.Label(root, text="Enter your name : ").grid(row=0,column=0)
name_label=ttk.Label(root, text="Enter your name : ")
name_label.grid(row=0,column=0,sticky=tk.W)
email_label=ttk.Label(root,text="Enter your email : ")
email_label.grid(row=1,column=0,sticky=tk.W)
age_label=ttk.Label(root,text="Enter you age : ")
age_label.grid(row=2,column=0,sticky=tk.W)
gender_label=ttk.Label(root, text="Select your gender : ")
gender_label.grid(row=3,column=0,sticky=tk.W)
profession_label=ttk.Label(root,text="Select your profession : ")
profession_label.grid(row=4,column=0,sticky=tk.W)
#varibles to store values of entryboxes
name_var=tk.StringVar()
email_var=tk.StringVar()
age_var=tk.StringVar()

#Entry box
name_entry=ttk.Entry(root, width=10,textvariable=name_var)
name_entry.grid(row=0,column=1)
name_entry.focus()
email_entry=ttk.Entry(root, width=10,textvariable=email_var)
email_entry.grid(row=1,column=1)
age_entry=ttk.Entry(root, width=10,textvariable=age_var)
age_entry.grid(row=2,column=1)

#Creating combobox

gender_var=tk.StringVar()
gender_combox=ttk.Combobox(root,width=10,textvariable=gender_var,state="readonly")
gender_combox["values"]=("Male","Female","Others")
gender_combox.current(0)
gender_combox.grid(row=3,column=1)

#Radio button
usertype=tk.StringVar()
radio_button1=ttk.Radiobutton(root,text="student",value="student",variable=usertype)
radio_button1.grid(row=4,column=1,sticky=tk.W)
radio_button2=ttk.Radiobutton(root,text="Teacher",value="Teacher",variable=usertype)
radio_button2.grid(row=5,column=1,sticky=tk.W)
radio_button3=ttk.Radiobutton(root,text="Principal",value="Principal",variable=usertype)
radio_button3.grid(row=6,column=1,sticky=tk.W)

#Checkbutton
English=tk.IntVar()
checkBtn1=ttk.Checkbutton(root,text="English",variable=English)
checkBtn1.grid(row=7,column=0,sticky=tk.W)
Hindi=tk.IntVar()
checkBtn2=ttk.Checkbutton(root,text="Hindi",variable=Hindi)
checkBtn2.grid(row=7,column=1)

#defining function for submit button action
#def action():
#    username=name_var.get()
#    userId=email_var.get()
#    userage=age_var.get()
#    usergender=gender_var.get()
#    userprofession=usertype.get()
#    english=English.get()
#    hindi=Hindi.get()
#    if English.get()==1 and Hindi.get()==1:
#        print("English")
#        print("Hindi")
#    elif English.get()==1 and Hindi.get()==0:
#        print("English")
#    elif English.get()==0 and Hindi.get()==1:
#        print("Hindi")
#    else:
#        pass
#    
#    print(f"{username} is {usergender} and {userage} years old,{userId}")
#    with open("TkinterData.txt","a") as f:
#        f.write(f"{username},{userId},{userage},{usergender},{userprofession},{english}{hindi}\n")
#        
#        #deleting input after submiting
#        name_entry.delete(0, tk.END)
#        email_entry.delete(0, tk.END)
#        age_entry.delete(0, tk.END)

#writing to csv file
def action():
    username=name_var.get()
    userId=email_var.get()
    userage=age_var.get()
    usergender=gender_var.get()
    userprofession=usertype.get()
    if English.get()==1:
        english="English"
    elif Hindi.get()==1:
        hindi="Hindi"
    else:
        pass
    with open("tkinterData.csv","a") as f:
        csv_writer=DictWriter(f,fieldnames=["Name","Email","Age","Gender","Profession","Language"])
        if os.stat("tkinterData.csv").st_size==0:
            csv_writer.writeheader()
        csv_writer.writerow(
        {"Name" : username , "Email" : userId, "Age" : userage, "Gender" : usergender, "Profession" : userprofession,"Language" : english }
        )
        
      
    
    

#creating button
submit_button=tk.Button(root, text="Submit",command=action)
submit_button.configure(foreground="blue",background="yellow")
submit_button.grid(row=8,column=0,sticky=tk.W)

#ttk.Label(root, text="Enter your name : ").pack()
root.mainloop()