def string(a):
    s=''
    # a='python'
    b=a[:2]+a[-2:]
    for i in b:
        s+=i+'.'
    return s
print(string(a=input("enter a word:")))