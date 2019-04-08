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
root.title("Admin")

def logout():
    os.system("main_login.py")

def showallrecords():

        r = Tk() # Opens new window
        r.geometry('1050x650') # Makes the window a certain size
        r.title('Welcome Administrator')

        rlbl = Label(r, text='\n Welcome Administrator')
        
        textLabel = Label(r, text="Id", width=10)
        textLabel.grid(row=0, column=0)
        intLabel = Label(r, text="Name", width=10)
        intLabel.grid(row=0, column=1)
        intLabel = Label(r, text="Email", width=10)
        intLabel.grid(row=0, column=2)
        intLabel = Label(r, text="Gender", width=10)
        intLabel.grid(row=0, column=3)
        intLabel = Label(r, text="Disorder", width=10)
        intLabel.grid(row=0, column=4)
        
        Data = readfromdatabase()
        for index, dat in enumerate(Data):
            Label(r, text=dat[0]).grid(row=index+1, column=0)
            Label(r, text=dat[1]).grid(row=index+1, column=1)
            Label(r, text=dat[2]).grid(row=index+1, column=2)
            Label(r, text=dat[3]).grid(row=index+1, column=3)

        r.mainloop()
            
def readfromdatabase():
        mycursor.execute("SELECT * FROM user")
        return mycursor.fetchall()

def login_btn_clicked():

    username = entryu.get()
    password = entryp.get()
        
    sql3 = "SELECT * FROM admin WHERE username = %s and password=%s"
    login = (username,password,)
    mycursor.execute(sql3, login)
    myresult = mycursor.fetchall()
    validate=len(myresult)
    if validate==1:
        for x in myresult:
            user_id=x[0]
            user_name=x[1]
        
        r = Tk() # Opens new window
        r.geometry('1050x650') # Makes the window a certain size
        r.title('Welcome Administrator')
        
        '''menu=Menu(r)
        r.config(menu=menu)
        
        submenu=Menu(menu)
        menu.add_cascade(label="Home",menu=submenu)
        submenu.add_command(label="User Details",command ="search")
        submenu.add_separator()
        submenu.add_command(label=" ",command ="")

        newmenu=Menu(menu)
        menu.add_cascade(label="Profile",menu=newmenu)
        newmenu.add_command(label="Logout",command =logout)
        
        rlbl = Label(r, text='\n Welcome Administrator')
        
        textLabel = Label(r, text="Id", width=10)
        textLabel.grid(row=0, column=0)
        intLabel = Label(r, text="Name", width=10)
        intLabel.grid(row=0, column=1)
        intLabel = Label(r, text="Email", width=10)
        intLabel.grid(row=0, column=2)
        intLabel = Label(r, text="Gender", width=10)
        intLabel.grid(row=0, column=3)
        intLabel = Label(r, text="Disorder", width=10)
        intLabel.grid(row=0, column=4)'''
        button1=Button(r,text="Show users",fg='blue',command=showallrecords).grid(row=1,column=3)

        button2=Button(r,text="Logout",fg='blue',command=logout).grid(row=1,column=4)


        #rlbl.pack()
        r.mainloop()
    else:
        tm.showerror("Login error", "Incorrect Username or Password")
        

labelt = Label(root, text="Admin Login", fg="Green",
                                font = ("calibri",20),width="20",height="3")
labelt.grid(row=0,sticky=E)

labelu = Label(root, text="Username")
labelu.grid(row=2,)

entryu = Entry(root)
entryu.grid(row=2, column=1)

labelp = Label(root, text="Password")
labelp.grid(row=3, )
        
entryp = Entry(root, show="*")
entryp.grid(row=3, column=1)

checkbox = Checkbutton(root, text="Keep me logged in")
checkbox.grid(row=5, columnspan=2)

logbtn_admin = Button(root, text="Admin Login",
                                     command=login_btn_clicked)
logbtn_admin.grid(row=7)

mainloop()
