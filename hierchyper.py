class person:
    def speak(self,name,age):
        self.name=name
        self.age=age
        print('the person is speaking')
class student(person):
    def study(self):
       pass 
class teacher(person):
    def teach(self):
        pass
obs=student()
obs.speak('aswin',23)
obs.study()
obt=teacher()
obt.speak('asd',12)
obt.teach()
    

        