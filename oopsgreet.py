class person:
    def greet(self,name,age,gender):
        
        self.name=name
        self.age=age
        self.gender=gender
        print('hello',self.name,'\n',self.age,'\n',self.gender)
ob=person()
ob.greet('aswin',22,'male')