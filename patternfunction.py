def pattern(a):
    for i in range(1,a+1):
        print('*'*i)
        print(end='')
    print()
pattern(a=int(input("enter a number:")))
