from tkinter import * 
root=Tk()
root.title("Home")
p=PhotoImage(file="bank1.png")
root.iconphoto(True,p)

root.geometry("600x400+360+150")
# root.resizable(0,0)


def func(arg):
    print(arg)

l=Label(root,text="This is the first button",font="helvetica")
l.pack(anchor=NW,ipadx=160,ipady=20,expand=True,side="left")


b=Button(root,text="Click me",command= lambda: func("You clicked it !"),bg="cyan",fg="black")
b.pack(anchor=NW,ipadx=10,ipady=10,side=LEFT,expand=True)

root.mainloop()