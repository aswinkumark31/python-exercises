class animal:
    def display(self,species,legs):
        self.species=species
        self.legs=legs
        print(self.species,self.legs)
class cat(animal):
    def dis(self,color):
        self.color=color
        print(self.color)
ob=cat()
ob.display('birds',2)
ob.dis('red')