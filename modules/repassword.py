import re

x=input('enter a word:')

a=re.search(r'[:word:]',x)
b=re.search(r'[\s]',x)
c=re.search(r'[^\w]',x)
d=re.search(r'[8>]',x)

if a:
    print('crt password')
elif b:
    print('crt password')
elif c:
    print(c)