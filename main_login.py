from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import mysql.connector
import os
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="project"
)

mycursor = mydb.cursor()

root = Tk()
root.geometry('1000x1000')


'''ent = Entry(root)
ent.pack()
ent.focus_set()'''

root.config(bg='green')

root.title("Main Page")

def adminlog():
    os.system("adminlog.py")

def userlog():
    os.system("userlog.py")


'''admin = PhotoImage(file = "admin.png")
a = Button(root,image=admin,command=adminlog)
a.grid(row=6,sticky=W)

label_admin = Label(root, text=" Administrator Login ", fg="blue",
                         font = ("calibri",10),width="20",height="1")
label_admin.grid(row=6,sticky=W)

label_space = Label(root, text="", fg="white",
                         font = ("calibri",10),width="160",height="1",bg="grey")
label_space.grid(row=8,)'''


text = Label(root, text="WELCOME TO THE WORLD OF SOCIAL MEDIA", fg="white",
                         font = ("calibri",20),width="80",height="3",bg="grey")
text.grid(row=0,columnspan=4)

admin = PhotoImage(file = "admin.png")
a = Button(root,image=admin,command="")
a.grid(row=2,column=0,padx=10,pady=10,sticky=W)

admin=Button(root,text="Admin Login",command=adminlog)
admin.grid(row=2,column=0,padx=35,pady=10,sticky=W)

user = PhotoImage(file = "user.png")
a = Button(root,image=user)
a.grid(row=3,column=0,padx=10,pady=10,sticky=W)

user=Button(root,text="User Login",command=userlog)
user.grid(row=3,column=0,padx=35,pady=10,sticky=W)


root.mainloop()
