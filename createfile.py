ob=open('demo.text','w')
ob.write('python')
ob.write('\njava')

ob=open('demo.text','r')
print(ob.read())

ob.close()