class triangle:
    a=30
    b=60
    c=90
    def angles(self):
        sum=self.a+self.b+self.c
        if sum==180:
            print('its a triangle')
        else:
            print('its not')
ob=triangle()
ob.angles()
        