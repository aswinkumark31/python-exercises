def display(n):
    if n==1:
        return n
    else:
        return n + display(n-1)
print(display(5)) 