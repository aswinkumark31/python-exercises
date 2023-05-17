ob=open('sample.text','w')
ob.write('python is interpreted')

ob=open('sample.text','r')
a=ob.read()

y=a.split()  
count=0
for i in y:
    count+=1
print(count)

ob.close()