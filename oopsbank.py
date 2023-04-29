class bank:
    l=[12,1324,246]
    balance=[300,500,200]
    
    def add(self,accountno):
        self.accountno=accountno
        self.l.append(accountno)
        print('account added successfully')
        
    def remove(self,accountno):
        self.accountno=accountno
        del self.l[2]
        print('account deleted')
        
    def display(self):
        print(self.l,self.balance)
        
ob=bank()
print('1.add \n 2.remove \n 3.account')
a=int(input('enter an option:'))
if a==1:
    ob.add(int(input('enter an account:')))
    print(ob.l)
elif a==2:
    ob.remove(int(input('enter a number:')))
elif a==3:
    ob.display()
else:
    print('invalid option please choose right one')
    
        
        