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
root.geometry('500x450')
root.title("Login")

def register_btn_clicked():
    os.system("userreg.py")

def logout():
    os.system("main_login.py")


    
def user_home():

    username = entry_username.get()
    password = entry_password.get()
        
    sql3 = "SELECT * FROM user WHERE username = %s and password=%s"
    login = (username,password,)
    mycursor.execute(sql3, login)
    myresult = mycursor.fetchall()
    validate=len(myresult)
    if validate==1:
        for x in myresult:
            user_id=x[0]
            user_name=x[1]
        r = Tk() # Opens new window
        r.title('Welcome '+user_name)
        r.geometry('1050x650') # Makes the window a certain size

        menu=Menu(r)
        r.config(menu=menu)

        newmenu=Menu(menu)
        menu.add_cascade(label="Home",menu=newmenu)
        newmenu.add_command(label="Logout",command =logout)
        
        submenu=Menu(menu)
        menu.add_cascade(label="Profile",menu=submenu)
        submenu.add_command(label="My Profile",command = "")
        submenu.add_separator()
        submenu.add_command(label=" ",command ="")

                
        rlbl = Label(r, text='\n Hi '+user_name)
        rlbl.pack()
        r.mainloop()
    else:
        tm.showerror("Login error", "Incorrect username")


def adminLogin():
    os.system("adminlog.py")


label_text = Label(root, text="User Login", fg="Green",
                                font = ("calibri",20),width="20",height="3")
label_text.grid(row=0,sticky=E)

label_username = Label(root, text="Username")
label_username.grid(row=2, )

entry_username = Entry(root)
entry_username.grid(row=2, column=1)

label_password = Label(root, text="Password")
label_password.grid(row=3, )

entry_password = Entry(root, show="*")
entry_password.grid(row=3, column=1)

checkbox = Checkbutton(root, text="Keep me logged in")
checkbox.grid(row=5, columnspan=2)

logbtn_user = Button(root, text="User Login",
                                  command=user_home) 
logbtn_user.grid(row=7, columnspan=2,sticky=E)

regbtn_user = Button(root, text="New User Register",
                                  command=register_btn_clicked)
regbtn_user.grid(row=7, columnspan=2)
        

root.mainloop()
