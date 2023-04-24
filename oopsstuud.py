class sample:
   
    def student(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
        print(self.name,self.age,self.rollno)
    def teacher(self,tname,tage,tdepartment):
        self.tname=tname
        self.tage=tage
        self.tdepartment=tdepartment
        print(self.tname,self.tage,self.tdepartment)
        print(self.age)
ob=sample()
ob.student('aswin',22,4)
ob.student('bibin',23,2)
ob.student('niza',23,2)
ob.teacher('asdg',30,'python')
