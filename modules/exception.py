
try:
    print(a)
except:
    print('a is not defined')
print('sucess')


# multiple exception handling

a = 10
b =2

try:
    z = a/b
    print(z)
    print(c)
except ZeroDivisionError:
    print('error!!')
except NameError:
    print('name error!!')
print('prgrm continue...')



try:
    print(a)
except:
    print('error!!')
finally:
    print('nothing happended')
