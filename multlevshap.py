class shape:
    def __init__(self,color):
        self.color=color
        print(self.color)
class rectangle(shape):
    def dis(self,width,height):
        self.width=width
        self.height=height
        print(self.width,self.height)
class square(rectangle):
    def display(self,width,height):
        self.width=width
        self.height=height
        print(self.width,self.height)
ob1 = shape('red')    
obr=rectangle()
obr.dis(4,6)
obs=square()
obs.dis(4,6)
obs.display(2,2)
