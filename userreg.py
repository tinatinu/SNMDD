from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="project"
)

mycursor = mydb.cursor()

root = Tk()
root.geometry("500x450")
root.title("Registration Form")

def login():
    os.system("main_login.py")

def registration():

    name=entry_name.get()
    email=entry_email.get()

    global selection
    selection=var.get()
         
    if selection == 1:
        gender="Male"
    elif selection == 2:
        gender="Female"
        
    username=entry_username.get()
    password=entry_password.get()
        
    add_user = ("INSERT INTO user "
                "(Name,Email,Gender,Username,Password)"
                "values(%s,%s,%s,%s,%s)")
    data_user = (name,email,gender,username,password)
    mycursor.execute(add_user, data_user)
    mydb.commit()

    tm.showinfo("Message","Details Entered Successfully")
    
    entry_name.config(text="")

    new =Tk()
    new.geometry("1000x1000")
    new.title("SNMDD")

    label_text = Label(new, text="To Continue Login Here", fg="Green",
            font = ("calibri",20),width="20",height="3")
    label_text.grid(row=0,sticky=E)
        
    logbtn_user = Button(new, text="Click here to Login",command=login) 
    logbtn_user.grid(row=5, )
        

label_text = Label(root, text="User Registration", fg="Green",
            font = ("calibri",20),width="20",height="3")
label_text.grid(row=0,sticky=E)

label_name = Label(root, text="Full Name")
label_name.grid(row=2,)

entry_name = Entry(root)
entry_name.grid(row=2,column=1)

label_email = Label(root, text="Email")
label_email.grid(row=3,)

entry_email = Entry(root)
entry_email.grid(row=3,column=1)

label_gender = Label(root, text="Gender")
label_gender.grid(row=4,)
var = IntVar()
Radiobutton(root,text="Male",padx=5,variable=var,value="1").grid(row=4,column=1)
Radiobutton(root,text="Female",padx=20,variable=var,
            value="2").grid(row=4,column=2)

label_username = Label(root, text="Username")
label_username.grid(row=5, )

entry_username = Entry(root)
entry_username.grid(row=5, column=1)

label_password = Label(root, text="Password")
label_password.grid(row=6, )

entry_password = Entry(root, show="*")
entry_password.grid(row=6, column=1)

logbtn_user = Button(root, text="User Login",command=registration) 
logbtn_user.grid(row=8, columnspan=2,)
        

mainloop()
