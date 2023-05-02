class employee:
    def display(self,name,salary):
        self.name=name
        self.salary=salary
        print(self.name,self.salary)
class manager(employee):
    def person(self,department):
        self.department=department
        print(self.department)
ob=manager()
ob.display('aswin',30000)
ob.person('python')