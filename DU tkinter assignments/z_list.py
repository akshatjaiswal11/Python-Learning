l=[1,2,3,6]
l2=[2,1,3,6]
ll=['akshat','Akshat']

print(l+l2)                     #        [1, 2, 3, 6, 2, 1, 3, 6]
print(max(l))                   #        6
print(min(l))                   #        1
print(max(ll))                  #        akshat
print(tuple(l))                 #        (1,2,3,6)


#           APPEND AND EXTEND

l=[1,2,4]                       #  we apply all these and print        
l.append([5])
l.append(7)
l.extend([8,9,10])        #             append([5])      extend([8,9,10])
print(l)                  #            [1, 2, 4, [5], 7, 8, 9, 10]

#reverse
l.reverse()         
print(l)                  #         [10, 9, 8, 7, [5], 4, 2, 1]

x=l.index(8)
print(x)
print(l.pop())   # after this we cannot pop element from list

l=[1,2,3,1,4]
l.remove(1)
print(l)                # [2,3,1,4]



a=sorted(l,reverse=True)            #sorted creates another sorted list
                                            # whereas 
                                    # sort modifies existing list and return None 
                                    #if we try to print

x=l.sort(reverse=True)
print(a,l)              #           [4, 3, 2, 1]      [4, 3, 2, 1]
print(x)                #               a                   l
#       print(x)   will print None


l=[1,2,3,4,5,2]
#del(l)
l.remove(3)
print(l)
