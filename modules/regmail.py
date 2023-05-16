import re

y=input('enter a word:')

a=re.search(r'[a-z0-9]',y)
b=re.search(r'[$@gmail.com]',y)
c=re.search(r'[$@yahoo.com]',y)

if b:
    print('valid email')
elif c:
    print('valid email')
else:
    print('invalid email')
