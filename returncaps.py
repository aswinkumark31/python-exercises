def string(a):
    count=0
    count1=0
    b=a.lower()
    for i in a:
        if i in b:
            count+=1
        else:
            count1+=1
    x=print('count of lower letters:',count,'count of upper letters:',count1)
    return x
print(string(a=input("enter a word:")))

