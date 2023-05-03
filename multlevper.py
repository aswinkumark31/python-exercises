class person:
    def display(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class employee(person):
    def dis(self,salary):
        self.salary=salary
        print(self.salary)
class manager(employee):
    def depat(self,department):
        self.department=department
        print(self.department)
        
obe=employee()
obe.display('aswin',22)
obe.dis(30000)
obm=manager()
obm.dis(4000)
obm.depat('coding')