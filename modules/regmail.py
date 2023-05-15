import re

a='abcd'
us = input('-')
b=re.search(r'[$@gmail.com]',us)

if b:
    print('yes')
else:
    print('no')