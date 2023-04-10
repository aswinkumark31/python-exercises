def fact(n):
    mult=1
    for i in range(1,n+1):
        mult*=i
    print(mult)

fact(n=int(input("enter a number:")))