f=open("f.txt","r")

x=f.read()
x=x.lower()

v="aeiou"
d=dict.fromkeys(v,0)

for i in x:
    if i in v:
        d[i]+=1
print(d)