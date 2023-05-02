class institution:
    def display(self):
        print('institute in kochi')
class department(institution):
    def dep(self,software):
       
        self.software=software
        print(self.software)
ob =department()
ob.display()
ob.dep('python,c')