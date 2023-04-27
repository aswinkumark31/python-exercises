class dog:
    def display(self,name,breed):
        self.name=name
        self.breed=breed
        print(self.name,self.breed)
    def bark(self):
        print('barking')
ob=dog()
ob.display('Leo','pitbull')
ob.bark()