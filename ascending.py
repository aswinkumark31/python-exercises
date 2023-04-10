a="python is interpreted"

l = a.split()
s = ''
for i in l:
    x = ''.join(sorted(i))
    s+=x + ' '
print(s)