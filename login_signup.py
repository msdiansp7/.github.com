import os
import tkinter
import tkinter as tk
from tkinter import ttk
from csv import DictReader,DictWriter
from tkinter import messagebox as m_box


root=tk.Tk()
root.title("Login and signup")

nb=ttk.Notebook(root)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text="Login Page")
nb.add(page2,text="Sign up Page")
nb.pack(expand=True,fill="both")

########### page 1 ###########

label_frame=ttk.LabelFrame(page1,text="Login")
label_frame.grid(row=0,column=0,padx=60,pady=200)


#labels

label1=ttk.Label(label_frame,text="Mobile : ",font=("Helvetica",10,"bold"))
label1.grid(row=0,column=0,pady=20,sticky=tk.W)

label2=ttk.Label(label_frame,text="Password : ",font=("Helvetica",10,"bold"))
label2.grid(row=0,column=1,pady=20,sticky=tk.W)

label3=ttk.Label(label_frame,text="Don't have an account ?")
label3.grid(row=3,columnspan=3,padx=70,pady=15)

#variables

name_var=tk.StringVar()
pass_var=tk.StringVar()
Bdate=tk.StringVar()
Bmonth=tk.StringVar()
Byear=tk.StringVar()
gender=tk.StringVar()
name=tk.StringVar()
email=tk.StringVar()
mobile=tk.StringVar()
AlterEmail=tk.StringVar()
Password=tk.StringVar()

#entrybox

entry1=ttk.Entry(label_frame,width=15,textvariable=name_var)
entry1.grid(row=1,column=0,padx=5,pady=10)

entry2=ttk.Entry(label_frame,width=15,textvariable=pass_var)
entry2.grid(row=1,column=1,padx=5,pady=10)

def Login():
    name=name_var.get()
    password=pass_var.get()
    with open("Users.csv","r") as f:
        csv_reader=DictReader(f)
        for row in csv_reader:
            if row["Mobile"]==name and row["Password"]:
                m_box.showinfo("Logged in","You have successfully logged in.")
                entry1.delete(0,tk.END)
                entry2.delete (0,tk.END)
            else:
                m_box.showerror("Error","Invalid username and password !!")
        
def newtab():
    page2.focus() 

button=tk.Button(label_frame,text="Log in",command=Login)
button.grid(row=2,columnspan=2,padx=100,pady=10)

button2=tk.Button(label_frame,text="Create an account",command=newtab)
button2.grid(row=4,columnspan=3,padx=100,pady=15)

########### Page 2 ###########

##On signup

def SignUp():
    username=name.get()
    mail=email.get()
    phone=mobile.get()
    AlterMail=AlterEmail.get()
    Pass=Password.get()
    Date=Bdate.get()
    Month=Bmonth.get()
    Year=Byear.get()
    Gender=gender.get()
    DOB=f"{Date}/{Month}/{Year}"
    with open("Users.csv","a") as f1:
        csv_writer=DictWriter(f1,fieldnames=["Name","Mail","Mobile","DOB","Gender","AlterMail","Password"])
        if os.stat("Users.csv").st_size==0:
            csv_writer.writeheader()
        
        csv_writer.writerow({
            "Name" : username,
            "Mail"   : mail,
            "Mobile": phone,
            "DOB"    : DOB,
            "Gender":Gender,
            "AlterMail": AlterMail,
            "Password" : Pass
            })
            
        entry3.delete(0,tk.END)
        entry4.delete(0,tk.END)
        entry5.delete(0,tk.END)
        entry8.delete(0,tk.END)
        entry9.delete(0,tk.END)




label_frame2=ttk.LabelFrame(page2,text="Signup")
label_frame2.grid(row=0,column=0,sticky=tk.W)

label3=ttk.Label(page2,text="Enter your name  ")
label3.grid(row=0,column=0,sticky=tk.W)

label4=ttk.Label(page2,text="Enter your email address  ")
label4.grid(row=1,column=0,sticky=tk.W)

label5=ttk.Label(page2,text="Enter your mobile number  ")
label5.grid(row=2,column=0,sticky=tk.W)

label6=ttk.Label(page2,text="Enter your date of birth ")
label6.grid(row=3,column=0,sticky=tk.W)

label7=ttk.Label(page2,text="Choose your gender ")
label7.grid(row=6,column=0,sticky=tk.W)

label8=ttk.Label(page2,text="Alternate Email address ")
label8.grid(row=7,column=0,sticky=tk.W)

label9=ttk.Label(page2,text="Choose your password ")
label9.grid(row=8,column=0,sticky=tk.W)

##Entry boxes

entry3=ttk.Entry(page2,width=20,textvariable=name)
entry3.grid(row=0,column=1,sticky=tk.W,pady=20)

entry4=ttk.Entry(page2,width=20,textvariable=email)
entry4.grid(row=1,column=1,sticky=tk.W,pady=20)

entry5=ttk.Entry(page2,width=20,textvariable=mobile)
entry5.grid(row=2,column=1,sticky=tk.W,pady=20)

combox1=ttk.Combobox(page2,width=5,textvariable=Bdate,state="readonly")
combox1["values"]=list(range(1,32))
combox1.current(28)
combox1.grid(row=3,column=1,sticky=tk.W,pady=20)

combox2=ttk.Combobox(page2,width=5,textvariable=Bmonth,state="readonly")
combox2["values"]=list(range(1,13))
combox2.current(0)
combox2.grid(row=4,column=1,sticky=tk.W,pady=20)

combox3=ttk.Combobox(page2,width=5,textvariable=Byear,state="readonly")
combox3["values"]=list(range(1979,2020))
combox3.current(0)
combox3.grid(row=5,column=1,sticky=tk.W,pady=20)

combox4=ttk.Combobox(page2,width=10,textvariable=gender,state="readonly")
combox4["values"]=["Male","Female","Others"]
combox4.current(0)
combox4.grid(row=6,column=1,sticky=tk.W,pady=20)

entry8=ttk.Entry(page2,width=20,textvariable=AlterEmail)
entry8.grid(row=7,column=1,sticky=tk.W,pady=20)

entry9=ttk.Entry(page2,width=20,textvariable=Password)
entry9.grid(row=8,column=1,sticky=tk.W,pady=25)

submit_btn=tk.Button(page2,text="Submit",command=SignUp)
submit_btn.grid(row=9,columnspan=4,padx=90)

root.mainloop()