# class hospital:
#     def display(self):
#         print('medicaltrust')
# class pharmacy(hospital):
#     def dep(self,medicines):
#         self.medicines=medicines
#         print(self.medicines)
# ob=pharmacy()
# ob.display()
# ob.dep('dfghj')


# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =age
    
#     def dis(self):
#         print(self.name,self.age)
        
# ob = person('aswin',23)

# ob.dis()

# __init__(self)


class sample:
    def __init__(self):
        print('welcome')
        self.a = 10
        self.b = 20
    def add(self):
        self.sum = self.a + self.b
        print(self.sum)  
ob1 = sample()
ob1.add()