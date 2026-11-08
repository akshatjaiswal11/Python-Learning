# *****-----            Bank Management System By Akshat Jaiswal         -----*****#

import mysql.connector as sql
from tkinter import *


win1=Tk()
win1.geometry("750x500+300+100")
win1.title("Maze Bank")
win1.resizable(0,0)

p1=PhotoImage(file="images/bank1.png")
win1.iconphoto(True,p1)

bg = PhotoImage(file="images/welcome_screen.png")
bgl=Label(win1,image=bg)
bgl.place(x=0,y=0,relwidth=1,relheight=1)

pic=PhotoImage(file="images/admin_button.png")
pic_l=Label(win1,image=pic,bg="#dfdede")
pic_l.place(x=380,y=260)

pic2=PhotoImage(file="images/customer_button.png")
pic2_l=Label(win1,image=pic2,bg="#dfdede")
pic2_l.place(x=570,y=260)


def open_admin_login():
    admin=Toplevel()
    admin.title("Admin Login")
    admin.geometry("750x500+300+100")
    admin.resizable(0,0)
    
    img=PhotoImage(file="images/admin_win.png")
    img_l=Label(admin,image=img)
    img_l.place(x=0,y=0)

    a_userval=StringVar()
    a_username=Entry(admin,width=15,bg="#c2eced",font="Helvetica 20",
                    textvariable=a_userval)
    a_username.place(x=500,y=195)
    
    a_passval=StringVar()
    a_password=Entry(admin,show="*",width=15,bg="#c2eced",font="helvetica 20",
                    textvariable=a_passval)
    a_password.place(x=500,y=295)

    
    def a_section():
        admin_sect=Toplevel()
        admin_sect.geometry("750x500+300+100")
        admin_sect.title("Admin Section")
        admin_sect.resizable(0,0)
        bg2=PhotoImage(file="images/section.png")
        bg2_l=Label(admin_sect,image=bg2)
        bg2_l.place(x=0,y=0)

        
        def new_user_acc():
            new_user=Toplevel()
            new_user.geometry("411x203+437+152")
            new_user.resizable(0,0)
            new_user.title("Create User Account")


            l1=Label(new_user,text="Full Name:")
            l1.place(relx=0.316, rely=0.099, height=27, width=75)

            fullname=StringVar()
            Entry1=Entry(new_user,background="#cae4ff",
                        textvariable=fullname)
            Entry1.place(relx=0.511, rely=0.099, height=20, relwidth=0.302)
            
            
            pin=StringVar()
            Entry2=Entry(new_user,background="#cae4ff",textvariable=pin)
            Entry2.place(relx=0.511, rely=0.253)


            repin=StringVar()
            Entry3=Entry(new_user,show="*",background="#cae4ff",textvariable=repin)
            Entry3.place(relx=0.511, rely=0.399)


            amount=IntVar()
            Entry4=Entry(new_user,background="#cae4ff",textvariable=amount)
            Entry4.place(relx=0.511, rely=0.65, height=20, relwidth=0.302)

            l2=Label(new_user,text="PIN:")
            l2.place(relx=0.399, rely=0.25, height=21, width=35)

            l3=Label(new_user,text="Re-enter PIN:")
            l3.place(relx=0.292, rely=0.39, height=21, width=75)

            l4=Label(new_user,text="Initial balance:")
            l4.place(relx=0.292, rely=0.64, height=21, width=75)

            l5=Label(new_user,text="User id number:")
            l5.place(relx=0.26, rely=0.5)


            mylist=[]
            for i in range(10000,100000):
                mylist.append(i)
            id_num=IntVar()
            Entry5=Entry(new_user,background="#cae4ff",textvariable=id_num)
            Entry5.place(relx=0.511, rely=0.525)
            

            b1=Button(new_user,text="Back",command=new_user.destroy)
            b1.place(relx=0.243, rely=0.85, height=24, width=67)


            def ok():
                u=fullname.get()
                am=amount.get()
                p=pin.get()
                rp=repin.get()
                id=id_num.get()
                pm=0
                mysql=sql.connect(host="localhost",user="root",password="123",database="bank")
                mycursor=mysql.cursor()
                s="select * from cust_login"
                mycursor.execute(s)
                a=[]
                for i in mycursor:
                    a.append(i)
                a_new=[]
                for i in a:
                    a_new.append(i[0])
                if u in a_new or len(str(u))==0 or str(u).isalpha==True or str(u).isnumeric==True:
                    pm+=1
                elif p!=rp:
                    pm+=1
                elif id not in mylist:
                    pm+=1
                elif am<0 and str(am).isdigit()!=True:
                    pm+=1
                else:
                    pass
                mysql=sql.connect(host="localhost",user="root",password="123", database="bank")
                qqq="select id from cust_login"
                cu=mysql.cursor()
                cu.execute(qqq)
                data=cu.fetchall()
                
                for i in data:
                    c=i[0]
                    if c==id:
                        pm+=11
                        break
                    else:
                        pm+0
                if pm>10:
                    root=Toplevel()
                    root.title("User ID exists")
                    root.geometry("350x100+500+280")
                    err=PhotoImage(file="images/error.png")
                    err_l=Label(root,image=err).place(x=20,y=10)

                    ll=Label(root,text="User ID exists",font="Helvetica 15 bold")
                    ll.place(x=120,y=35)
                    root.mainloop()
                    
    
                if pm==0:
                    mysql=sql.connect(host="localhost",user="root",password="123", database="bank")
                    mycursor=mysql.cursor()
                    q="insert into cust_login values(%s,%s,%s,%s)"
                    val=(id,str(u),str(p),int(am))
                    mycursor.execute(q,val)
                    mysql.commit()
                    root=Toplevel()
                    root.title("Account created")
                    root.geometry("350x100+500+280")
                    ll=Label(root,text="Success! Account created ",font="Helvetica 15 bold")
                    ll.place(x=50,y=35)
                    root.mainloop()

                elif pm>=1 and pm<10:
                    root=Toplevel()
                    root.title("Invalid Enteries")
                    root.geometry("350x100+500+280")
                    err=PhotoImage(file="images/error.png")
                    err_l=Label(root,image=err).place(x=20,y=10)

                    ll=Label(root,text="Please reassure enteries",font="Helvetica 15 bold")
                    ll.place(x=120,y=35)
                    root.mainloop()

            b2=Button(new_user,text="Proceed",command=ok)
            b2.place(relx=0.633, rely=0.85, height=24, width=67)

            new_user.mainloop()
    

        new_user_img=PhotoImage(file="images/1new_user.png")
        new_user_img_l=Label(admin_sect,image=new_user_img,bg="#f3c58e")
        new_user_button=Button(admin_sect,image=new_user_img,
                            borderwidth=0,command=new_user_acc,
                                bg="#f3c58e")
        new_user_button.place(x=30,y=40)


        def check_status():
            check_status_win=Toplevel()
            check_status_win.geometry("411x117+504+268")
            check_status_win.title("Check Status")

            uname=StringVar()
            Entry1=Entry(check_status_win,background="#cae4ff",textvariable=uname)
            Entry1.place(relx=0.487, rely=0.25, height=20, relwidth=0.277)

            l1=Label(check_status_win,text="Enter Username:")
            l1.place(relx=0.219, rely=0.25, height=21, width=104)

            b1=Button(check_status_win,text="Back",command=check_status_win.destroy)
            b1.place(relx=0.243, rely=0.642, height=24, width=67)


            def checking():
                mysql=sql.connect(host="localhost",user="root",password="123",database="bank")
                mycursor=mysql.cursor()
                u=str(uname.get())
                s="select * from cust_login where uname=%s"
                val=(u,)
                mycursor.execute(s,val)
                data=mycursor.fetchall()
                a=[]
                for i in data:
                    a.append(i)
                if a==[]:
                    root=Toplevel()
                    root.title("Invalid Credentials")
                    root.geometry("350x100+500+280")
                    err=PhotoImage(file="images/error.png")
                    err_l=Label(root,image=err).place(x=20,y=10)

                    ll=Label(root,text="Invalid credentials!!",font="Helvetica 15 bold")
                    ll.place(x=120,y=35)
                    root.mainloop()

                    
                else:
                    aa=a[0]
                    aal=list(aa)
                    x=aal[0]
                    y=aal[1]
                    z=aal[2]
                    zz=aal[3]
                    checking_win=Toplevel()
                    checking_win.geometry("411x117+504+268")
                    l1=Label(checking_win,text="Account ID:").place(x=10,y=10)
                    l2=Label(checking_win,text="Username:").place(x=10,y=40)
                    #l3=Label(checking_win,text="Password:").place(x=10,y=70)
                    l4=Label(checking_win,text="Amount").place(x=200,y=10)

                    l_1=Label(checking_win,text=x).place(x=100,y=10)
                    l_2=Label(checking_win,text=y).place(x=100,y=40)
                    #l_3=Label(checking_win,text=z).place(x=100,y=70)
                    l_4=Label(checking_win,text=zz).place(x=300,y=10)

            
            b2=Button(check_status_win,text="Proceed",command=checking)
            b2.place(relx=0.608, rely=0.642, height=24, width=67)


            check_status_win.mainloop()


        check_status_img=PhotoImage(file="images/2status.png")
        check_status_l=Label(admin_sect,image=check_status_img,bg="#f3c58e")
        check_status_button=Button(admin_sect,image=check_status_img,borderwidth=0,
                                    command=check_status,
                                    bg="#f3c58e")
        check_status_button.place(x=265,y=40)

        
        def terminate():
            balance_win=Toplevel()
            balance_win.geometry("411x117+504+268")
            balance_win.title("Terminate Account")
            
            uname=StringVar()
            Entry1=Entry(balance_win,background="#cae4ff",textvariable=uname)
            Entry1.place(relx=0.487, rely=0.092, height=20, relwidth=0.277)

            l1=Label(balance_win,text="Enter Username:")
            l1.place(relx=0.219, rely=0.092, height=21, width=104)

            l2=Label(balance_win,text="Re Enter Username:")
            l2.place(relx=0.209, rely=0.33, height=21, width=109)

            reuname=StringVar()
            Entry1_1=Entry(balance_win,background="#cae4ff",textvariable=reuname)
            Entry1_1.place(relx=0.487, rely=0.33, height=20, relwidth=0.277)

            b1=Button(balance_win,text="Back",command=balance_win.destroy)
            b1.place(relx=0.243, rely=0.642, height=24, width=67)

            
            
            def terminating():
                mysql=sql.connect(host="localhost",user="root",password="123",database="bank")
                mycursor=mysql.cursor()
                q="select * from cust_login"
                mycursor.execute(q)
                data=mycursor.fetchall()
                a=[]
                for i in data:
                    a.append(i[1])

                if str(uname.get()) not in a:
                        root=Toplevel()
                        root.title("Invalid Credentials")
                        root.geometry("350x100+500+280")
                        err=PhotoImage(file="images/error.png")
                        err_l=Label(root,image=err).place(x=20,y=10)

                        ll=Label(root,text="Invalid credentials!!",font="Helvetica 15 bold")
                        ll.place(x=120,y=35)
                        root.mainloop()
                else:
                    q="delete from cust_login where uname=%s"
                    u=str(uname.get())
                    val=(u,)
                    mycursor.execute(q,val)
                    mysql.commit()
                    root=Toplevel()
                    root.title("Account Terminated")
                    root.geometry("350x100+500+280")
                    err=PhotoImage(file="images/error.png")
                    err_l=Label(root,image=err).place(x=20,y=10)
                    ll=Label(root,text="""Success Account 
        Terminated""",font="Helvetica 15 bold")
                    ll.place(x=120,y=35)
                    root.mainloop()
            
            b2=Button(balance_win,text="Proceed",command=terminating)
            b2.place(relx=0.608, rely=0.642, height=24, width=67)

            balance_win.mainloop()


        terminate_img=PhotoImage(file="images/3terminate.png")
        terminate_img_l=Label(admin_sect,image=terminate_img,bg="#f3c58e")
        terminate_button=Button(admin_sect,image=terminate_img,
                            borderwidth=0,bg="#f3c58e",command=terminate)
        terminate_button.place(x=500,y=38)

        a_exit_img=PhotoImage(file="images/5exit.png")
        a_exit_img_l=Label(admin_sect,image=a_exit_img,bg="#f3c58e")
        a_exit_button=Button(admin_sect,image=a_exit_img,
                            borderwidth=0,bg="#f3c58e",command=admin_sect.destroy)
        a_exit_button.place(x=265,y=168)


        admin_sect.mainloop()

    def a_login_ok():
        mysql=sql.connect(host="localhost",user="root",password="123",database="bank")
        mycursor=mysql.cursor()
        uname=a_userval.get()
        password=a_passval.get()
        s="select * from admin_login where uname= %s and password=%s"
        mycursor.execute(s, [(uname),str((password))])
        results=mycursor.fetchall()

        if results:
            a_section()
        else:
            root=Toplevel()
            root.title("Invalid Credentials")
            root.geometry("350x100+500+280")
            err=PhotoImage(file="images/error.png")
            err_l=Label(root,image=err).place(x=20,y=10)

            ll=Label(root,text="Invalid credentials!! ...",font="Helvetica 15 bold")
            ll.place(x=120,y=35)
            root.mainloop()


    a_login_img=PhotoImage(file="images/login.png")
    
    a_login_button=Button(admin,image=a_login_img,command=a_login_ok,borderwidth=0,bg="white",highlightcolor="white")
    a_login_button.place(x=580,y=370)

    def a_signin_ok():
        mysql=sql.connect(host="localhost",user="root",password="123",database="bank")
        mycursor=mysql.cursor()
        uname=a_userval.get()
        password=a_passval.get()
        s="select * from admin_login"
        mycursor.execute(s)
        a=[]
        for i in mycursor:
            a.append(i)
        a_new=[]
        for i in a:
            a_new.append(i[0])

        if len(uname)==0 or len(password)==0:
            root=Toplevel()
            root.title("Invalid Credentials")
            root.geometry("350x100+500+280")
            err=PhotoImage(file="images/error.png")
            err_l=Label(root,image=err).place(x=20,y=10)
            ll=Label(root,text="Invalid credentials!! ...",font="Helvetica 15 bold")
            ll.place(x=120,y=35)
            root.mainloop()
            
        elif uname in a_new:
            root=Toplevel()
            root.title("Username exists")
            root.geometry("350x100+500+280")
            ll=Label(root,text="""Username Exists !!!
    Please use another username""",font="Helvetica 15 bold")
            ll.place(x=2,y=20)
            root.mainloop()
        else:
            q="insert into admin_login(uname, password) values(%s,%s)"
            val=(str(uname),str(password))
            mycursor.execute(q,val)
            mysql.commit()
            a_section()
    a_sign_img=PhotoImage(file="images/signup.png")
    
    a_sign_button=Button(admin,image=a_sign_img,command=a_signin_ok,borderwidth=0,bg="white",highlightcolor="white")
    a_sign_button.place(x=400,y=370)

    
    a_back_img=PhotoImage(file="images/back_button.png")
    a_back_button=Button(admin,image=a_back_img,command=admin.destroy,borderwidth=0,bg="white")
    a_back_button.place(x=320,y=375)


    admin.mainloop()


def customer_login():
    customer=Toplevel()
    customer.geometry("750x500+300+100")
    customer.title("Customer Login")

    img2=PhotoImage(file="images/customer_win.png")
    img2_l=Label(customer,image=img2)
    img2_l.place(x=0,y=0)

    c_userval=StringVar()
    c_username=Entry(customer,width=15,bg="#c2eced",font="Helvetica 20",
                    textvariable=c_userval)
    c_username.place(x=500,y=195)
    

    c_passval=StringVar()
    c_password=Entry(customer,show="*",width=15,bg="#c2eced",font="helvetica 20",
                    textvariable=c_passval)
    c_password.place(x=500,y=295)

    
    def c_section():
        cust_sect=Toplevel()
        cust_sect.geometry("750x500+300+100")
        cust_sect.title("Customer Section")
        cust_sect.resizable(0,0)
        
        bg2=PhotoImage(file="images/section.png")
        bg2_l=Label(cust_sect,image=bg2)
        bg2_l.place(x=0,y=0)


        def deposit():
            deposit_win=Toplevel()
            deposit_win.geometry("411x117+504+268")
            deposit_win.title("Deposit Amount")

            l2=Label(deposit_win,text="Enter Amount:")
            l2.place(relx=0.209, rely=0.33, height=21, width=109)

            amount=IntVar()
            Entry1_1=Entry(deposit_win,background="#cae4ff",textvariable=amount)
            Entry1_1.place(relx=0.487, rely=0.33, height=20, relwidth=0.277)

            b1=Button(deposit_win,text="Back",command=deposit_win.destroy)
            b1.place(relx=0.243, rely=0.642, height=24, width=67)
            def depositing():
                mysql=sql.connect(host="localhost",user="root",password="123",database="bank")
                mycursor=mysql.cursor()
                qq="select amount from cust_login where uname=%s"
                val=(str(c_username.get()),)
                mycursor.execute(qq,val)
                data=mycursor.fetchall()
                a=data[0]
                al=list(a)
                all=al[0]
                new_amount=int(int(all)+amount.get())
                mycursor1=mysql.cursor()
                q="update cust_login set amount=%s where uname=%s"
                val=(new_amount,str(c_username.get()))
                mycursor1.execute(q,val)
                mysql.commit()
                root=Toplevel()
                root.title("Amount Deposited")
                root.geometry("350x100+500+280")
                ll=Label(root,text="Amount deposited",font="Helvetica 15 bold")
                ll.place(x=120,y=35)
                root.mainloop()

                    
            b2=Button(deposit_win,text="Deposit",command=depositing)
            b2.place(relx=0.608, rely=0.642, height=24, width=67)


            deposit_win.mainloop()
        

        deposit_img=PhotoImage(file="images/deposit_.png")
        deposit_img_l=Label(cust_sect,image=deposit_img,bg="#f3c58e")
        deposit_button=Button(cust_sect,image=deposit_img,
                            borderwidth=0,
                            bg="#f3c58e",
                            command=deposit)
        deposit_button.place(x=30,y=40)


        def withdraw():
            withdraw_win=Toplevel()
            withdraw_win.geometry("411x117+504+268")
            withdraw_win.title("Withdraw Amount")

            l2=Label(withdraw_win,text="Enter Amount:")
            l2.place(relx=0.209, rely=0.33, height=21, width=109)

            amount=IntVar()
            Entry1_1=Entry(withdraw_win,background="#cae4ff",textvariable=amount)
            Entry1_1.place(relx=0.487, rely=0.33, height=20, relwidth=0.277)

            b1=Button(withdraw_win,text="Back",command=withdraw_win.destroy)
            b1.place(relx=0.243, rely=0.642, height=24, width=67)


            def withdrawing():
                mysql=sql.connect(host="localhost",user="root",password="123",database="bank")
                mycursor=mysql.cursor()
                qq="select amount from cust_login where uname=%s"
                val=(str(c_username.get()),)
                mycursor.execute(qq,val)
                data=mycursor.fetchall()
                a=data[0]
                al=list(a)
                all=al[0]
                if amount.get()<0:
                        root=Toplevel()
                        root.title("Invalid Credentials")
                        root.geometry("350x100+500+280")
                        err=PhotoImage(file="images/error.png")
                        err_l=Label(root,image=err).place(x=20,y=10)
            
                        ll=Label(root,text="Invalid credentials!! ...",font="Helvetica 15 bold")
                        ll.place(x=120,y=35)
                        root.mainloop()

                else:
                    new_amount=int(int(all)-amount.get())
                    mycursor1=mysql.cursor()
                    q="update cust_login set amount=%s where uname=%s"
                    val=(new_amount,str(c_username.get()))
                    mycursor1.execute(q,val)
                    mysql.commit()
                    root=Toplevel()
                    root.title("Amount withdrawn")
                    root.geometry("350x100+500+280")
                    ll=Label(root,text="Amount withdrawn",font="Helvetica 15 bold")
                    ll.place(x=120,y=35)
                    root.mainloop()
                
            b2=Button(withdraw_win,text="Withdraw",command=withdrawing)
            b2.place(relx=0.608, rely=0.642, height=24, width=67)


            withdraw_win.mainloop()


        withdraw_img=PhotoImage(file="images/withdraw.png")
        withdraw_img_l=Label(cust_sect,image=withdraw_img,bg="#f3c58e")
        withdraw_button=Button(cust_sect,image=withdraw_img,
                            borderwidth=0,
                            bg="#f3c58e",
                            command=withdraw)
        withdraw_button.place(x=265,y=40)
        def balance():
            u=str(c_userval.get())
            mysql=sql.connect(host="localhost",user="root",password="123",database="bank")
            mycursor=mysql.cursor()
            q="select * from cust_login where uname=%s"
            val=(u,)
            mycursor.execute(q,val)
            data=mycursor.fetchall()
            a=[]
            for i in data:
                a.append(i)
            aa=a[0]
            aal=list(aa)


            x=aal[0]
            y=aal[1]
            z=aal[2]
            zz=aal[3]
            checking_win=Toplevel()
            checking_win.geometry("411x117+504+268")
            l1=Label(checking_win,text="UAccount ID:").place(x=10,y=10)
            l2=Label(checking_win,text="Username:").place(x=10,y=40)
            l3=Label(checking_win,text="Password:").place(x=10,y=70)
            l4=Label(checking_win,text="Amount:").place(x=200,y=10)
            l_1=Label(checking_win,text=x).place(x=100,y=10)
            l_2=Label(checking_win,text=y).place(x=100,y=40)
            l_3=Label(checking_win,text=z).place(x=100,y=70)
            l_4=Label(checking_win,text=zz).place(x=300,y=10)

        balance_img=PhotoImage(file="images/balance.png")
        balance_img_l=Label(cust_sect,image=balance_img,bg="#f3c58e")
        balance_button=Button(cust_sect,image=balance_img,
                            borderwidth=0,bg="#f3c58e",command=balance)
        balance_button.place(x=500,y=38)


        exit_img=PhotoImage(file="images/exit.png")
        exit_img_l=Label(cust_sect,image=exit_img,bg="#f3c58e")
        exit_button=Button(cust_sect,image=exit_img,
                            borderwidth=0,bg="#f3c58e"
                            ,command=cust_sect.destroy)
        exit_button.place(x=265,y=168)


        cust_sect.mainloop()

    def c_login_ok():
        mysql=sql.connect(host="localhost",user="root",password="123",database="bank")
        mycursor=mysql.cursor()
        uname=c_userval.get()
        password=c_passval.get()
        s="select * from cust_login where uname= %s and password=%s"
        mycursor.execute(s, [(uname),str((password))])
        results=mycursor.fetchall()

        if results:
            c_section()
        else:
            root=Toplevel()
            root.title("Invalid Credentials")
            root.geometry("350x100+500+280")
            err=PhotoImage(file="images/error.png")
            err_l=Label(root,image=err).place(x=20,y=10)

            ll=Label(root,text="Invalid credentials!! ...",font="Helvetica 15 bold")
            ll.place(x=120,y=35)
            root.mainloop()


    c_login_img=PhotoImage(file="images/login.png")
    
    c_login_button=Button(customer,image=c_login_img,command=c_login_ok,borderwidth=0,bg="white",highlightcolor="white")
    c_login_button.place(x=530,y=370)

    c_back_img=PhotoImage(file="images/back_button.png")
    c_back_button=Button(customer,image=c_back_img,command=customer.destroy,borderwidth=0,bg="white")
    c_back_button.place(x=320,y=375)


    customer.mainloop()


admin_button=Button(win1,image=pic,command=open_admin_login,borderwidth=0,
                    bg="#dfdede")
admin_button.place(x=380,y=260)

customer_button=Button(win1,image=pic2,command=customer_login,borderwidth=0,
                    bg="#dfdede")
customer_button.place(x=570,y=260)


win1.mainloop()

# *****-----            Bank Management System By Akshat Jaiswal        -----*****#
