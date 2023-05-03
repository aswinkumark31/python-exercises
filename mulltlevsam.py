class school:
    def dis(self,name):
        self.name=name
        print(self.name)
        
class teacher(school):
    def display(self,name,salary):
        self.name=name
        self.salary=salary
        print(self.name,self.salary)
        
class department(teacher):
    def depart(self,course):
        self.course=course
        print(self.course)
ob=teacher()
ob.dis('Siena college')
ob.display('asd',30000)
obd=department()
# obd.display('asd',20000)
obd.depart('python')
