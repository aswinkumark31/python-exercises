class bank:
    l=[12,1324,246]
    def add(self,accountno):
        
        self.accountno=accountno
        self.l.append(accountno)
        print('account added successfully')
    def remove(self,accountno):
        self.accountno=accountno
        del self.l[2]
        print('account deleted')
ob=bank()
print('1.add \n 2.remove')
a=int(input('enter an option:'))
if a==1:
    ob.add(int(input('enter an account:')))
    print(ob.l)
else:
    ob.remove(int(input('enter a number:')))
        
        