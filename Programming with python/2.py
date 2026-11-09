# n=int(input("Entre the number -> "))

# for i in range(2,n+1):
#     t=0
#     for j in range(2,i):
#         if(i%j==0):
#             t+=1
#             break
#     if(t==0):
#         print(i,end=" ")
     
     
n=int(input("Enter a number :"))
# we have to print all the numbers before n that are prime

def prime(n):
    x= True
    for i in range(2,n):
        if(n%i==0):
            x=False
            break
    return x



if(n<=0):
    print("Not a valid number")
elif(n==1):
    pass
else:
    for i in range(2,n+1):
        if (prime(i) == True):
            print(i,end=" ")

