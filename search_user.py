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

root=Tk()
root.geometry('1000x1000')

def showallrecords():
        Data = readfromdatabase()
        for index, dat in enumerate(Data):
            Label(root, text=dat[0]).grid(row=index+1, column=0)
            Label(root, text=dat[1]).grid(row=index+1, column=1)
            Label(root, text=dat[2]).grid(row=index+1, column=2)
            Label(root, text=dat[3]).grid(row=index+1, column=3)
            
def readfromdatabase():
        mycursor.execute("SELECT * FROM user")
        return mycursor.fetchall()

'''class Records():
    def __init__(self, master):
        self.master = master
        self.master.geometry('1000x1000')
        self.master.title('Records')
        self.connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="project"
)

        self.mycursor = self.connection.cursor()'''
textLabel = Label(root.master, text="Id", width=10)
textLabel.grid(row=0, column=0)
intLabel = Label(root, text="Name", width=10)
intLabel.grid(row=0, column=1)
intLabel = Label(root, text="Email", width=10)
intLabel.grid(row=0, column=2)
intLabel = Label(root, text="Gender", width=10)
intLabel.grid(row=0, column=3)
intLabel = Label(root, text="Disorder", width=10)
intLabel.grid(row=0, column=4)
button2=Button(root,text="Show",fg='blue',command=showallrecords).grid(row=2,column=6)


  '''def search_user():
    os.system("search_user.py")
    

def search():
    #os.system("search_user.py")
    label1=Label(r,text='Main Menu',fg='red').grid(row=0,column=1)
        #self.button1=Button(self.master,text="Enter Data",fg='green',command=self.gotodataentry).grid(row=1,column=1)
    button2=Button(r,text="Data Records",fg='blue',command=search_user).grid(row=2,column=1)
        #button3=Button(self.master,text="Exit",fg='red',command=self.exit).grid(row=3,column=1)

'''  


