class circle:
    def circumferences(self,r):
        self.PI=3.14
        self.r=r
        self.x=2*self.PI*self.r
        return self.x
    def area(self,r):
        self.PI=3.14
        self.r=r
        self.c=self.PI*self.r**2
        return self.c
ob=circle()
print(ob.circumferences(int(input('enter a value:'))))
print(ob.area(3))