class bank:
    balance=500
    def display(self,name,accountno):
        self.name=name
        self.accountno=accountno
        
   
    def deposit(self,depo):
       
        self.depo=depo
        x=self.balance+depo
        print('your current balance is ',x)
    def withdraw(self,withdrawal):
      
        self.withdrawal=withdrawal
        y=self.balance-withdrawal
        print('your current balance is ',y)
ob=bank()
ob.display(input('enter a name:'),int(input('enter accountno:')))
print('1.balance\n 2.deposit\n 3.withdraw')
a=int(input('enter an option:'))
if a==1:
    print('your balnce is ', ob.balance)
elif a==2:
    ob.deposit(100)
else:
    ob.withdraw(200)

