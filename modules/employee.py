class employee:
    def display(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        print(self.name,self.age,self.salary)
        
    def get_name(self,name):
        self.name=name
        print('the name of the employee is',self.name)
        
    def get_age(self,age):
        self.age=age
        print('the age of the employee is',self.age)
        
    def get_salary(self,salary):
        self.salary=salary
        print('salary is',self.salary)
ob=employee()
