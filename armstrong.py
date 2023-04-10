n=input ("enter a number:")
y=0
for i in range(len(n)):
    x=int(n[i])
    # print(x)
    z=x**3
    y+=z
print(y)