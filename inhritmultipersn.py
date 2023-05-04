class person:
    def display(self,name):
        self.name=name
        print(self.name)
class cancook:
    def cook(self):
        pass
class canpaint:
    def paint(self):
        pass
class chef(person,cancook,canpaint):
    def dis(self,speciality):
        self.speciality=speciality
        print(self.speciality)
ob=chef()
ob.display('aswin')
ob.dis('good taste')
