class shape:
    def display(self,color,size):
        self.color=color
        self.size=size
        print(self.color,self.size)
class circle(shape):
    def dis(self,radius):
        self.radius=radius
        print('radius is' ,self.radius)
ob=circle()
ob.display('red',4)
ob.dis(4)