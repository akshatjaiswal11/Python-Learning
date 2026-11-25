
def prime(n):
    x= True
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            x=False
            break
    return x

n=int(input("Enter a number :"))
count = 0
num=2
while(count<n):
    if(prime(num)):
        print(num,end=" ")
        count+=1
    num+=1