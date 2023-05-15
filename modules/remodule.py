import re

# print(re.search(r'[0-9]','123'))
# print(re.search(r'[0-9]','abcd'))
# print(re.search(r'[a-z,0-9]','123a'))

if re.search(r'[^P]','Pasd'):
    print('yes!!')
else:
    print('No!!!')

a=re.search(r'[$P]','asfP')
if a:
    print('yes')
else:
    print('no')