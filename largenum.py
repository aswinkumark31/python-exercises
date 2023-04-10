
def largenum(b):
    
    l=[]
    n=0
    
    for i in range(1,b+1):
        a=int(input("enter a number:"))
        l.append(a)
    for j in l:  
        if j>n: 
            n=j 
    print(n) 
largenum(b=int(input("enter a limit:"))) 


# l=[]
# for i in  range(1,4):
#     n=int(input("enter a number:"))
#     l.append(n)
# print(l) 



