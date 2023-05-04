class shape:
    def __init__(self,color):
        self.color=color
        print(self.color)
class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        print(self.width,self.height)
class square(rectangle):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        print(self.width,self.height)
ob=shape('red')
ob1=rectangle(4,6)
ob2=square(2,2)


# class A:
#     def __init__(self,name):
#         self.name = name
#         print(self.name)
# class B(A):
#     def __init__(self, age):
#         self.age = age
#         print(self.age)
# ob1 = A('aswin')
# ob = B(25)
        
        

