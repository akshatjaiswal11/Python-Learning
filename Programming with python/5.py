l=[1,2,3,2,4,3,2,6,4,6,6,6]
d={}

for i in l:
    if i not in d:
        f=0
        t=i
        for j in l:
            if(t==j):
                f+=1
        d[t]=f
print(d)