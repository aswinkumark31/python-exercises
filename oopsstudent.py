class student:
   
    def setd(self):
        self.name=input('enter a name:')
        self.age=int(input('enter your age:'))
        self.grade=input('enter your grade:')
    def getd(self):
        print('your name is',self.name)
        print('your age is',self.age)
        print('your grade is',self.grade)
        
ob=student()
ob.setd()
ob.getd()