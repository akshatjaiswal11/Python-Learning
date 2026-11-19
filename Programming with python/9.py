f1=open("f1.txt","r")
f2=open("f2.txt","r")
f3=open("f3.txt","r")
f=open("f.txt","w")

x=f1.read()
x2=f2.read()
x3=f3.read()

l=[x,x2,x3]

f.writelines(l)
f.close()
