s1=lambda a,b:a*b


s2=lambda a,b:a/b


s3=lambda a,b:a-b

s4=lambda a,b:a+b


print('1.multiplication,2.division,3.substraction,4.sum')
x=int(input('enter a option:'))
y=int(input('enter a number:'))
z=int(input('enter a number:'))

if x==1:
    print(s1(y,z))
elif x==2:
    print(s2(y,z))
elif x==3:
    print(s3(y,z))
else:
    print(s4(y,z))


