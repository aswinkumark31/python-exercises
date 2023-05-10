import math

x1=int(input('enter a number:'))
x2=int(input('enter a number:'))
y1=int(input('enter a number:'))
y2=int(input('enter a number:'))

c= math.pow((x1-x2),2) + math.pow((y1-y2),2)
d=math.sqrt(c)
print(d)
