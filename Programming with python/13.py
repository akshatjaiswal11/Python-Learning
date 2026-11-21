from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

root=Tk()
root.geometry("600x400+360+150")
root.resizable(0,0)
root.title("Entry form")

f=Frame(root)
f.pack()

f_1=LabelFrame(f,text="User Info")
f_1.grid(row=0,column=0)

title=Label(f_1,text="Title")
usrn=Label(f_1,text="First Name")
lstn=Label(f_1,text="Last Name")
age=Label(f_1,text="Age")


title.grid(row=0,column=0)
usrn.grid(row=0,column=1)
lstn.grid(row=0,column=2)
age.grid(row=2,column=0)

title_c=ttk.Combobox(f_1,values=["","Dr.","Mr","Ms.","Mrs."])
title_c.grid(row=1,column=0)

usrn_e=Entry(f_1,font=("calibre"))
usrn_e.grid(row=1,column=1)

lstn_e=Entry(f_1,font=("calibre"))
lstn_e.grid(row=1,column=2)

age_spin=Spinbox(f_1,from_=18,to=100)
age_spin.grid(row=3,column=0)

for widget in f_1.winfo_children():
    widget.grid_configure(padx=20,pady=10)

























































root.mainloop()