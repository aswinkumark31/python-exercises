class sample:
    a=10
    b=2
    def display(self,c):
        self.c = c
        print(c)
        
        print(self.a,self.b)
    def sum(self):
        print(self.c)
        sum=self.a+self.b
        print(sum)
    def sub(self):
        sub=self.a-self.b
        print(sub)
    def mult(self):
        mult=self.a*self.b
        print(mult)
    def div(self):
        div=self.a/self.b
        print(div)
ob=sample()
ob.display(3)
ob.sum()
ob.sub()
ob.mult()
ob.div()
