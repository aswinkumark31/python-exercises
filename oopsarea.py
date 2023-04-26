class rectangle:
    def area(self,width,height):
        self.width=width
        self.height=height
        print('area',width*height)
ob=rectangle()
ob.area(5,6)