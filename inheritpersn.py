class person:
    def display(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class student(person):
    def dis(self,grade):
        self.grade=grade
        print(self.grade)
ob=student()
ob.display('aswin',22)
ob.dis('A')
    
        