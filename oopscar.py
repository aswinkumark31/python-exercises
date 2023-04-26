class car:
    
    def display(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        print(self.make,self.model,self.year)
    def start(self):
        print('car is running')
    def stop(self):
        print('car stopped')
    # def check():
    #     print('start/stop')

        
ob=car()
ob.display('asd','cd11',2023)
print('1.start \n 2.stop')
x=input('enter a word:')
if x=='start':
    ob.start()
else:
    ob.stop()
    
  