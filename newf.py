def display(n):
    if n==1:
        return n
    else:
        return n * display(n-1)

d=display(5)
print(d)


