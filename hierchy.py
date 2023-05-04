class vehicle:
    def start_engine(self,brand,model):
        self.brand=brand
        self.model=model
        print('the engine has started')
class car(vehicle):
    def drive(self,color,seats):
        self.color=color
        self.seats=seats
        print('car is being driven')
class bike(vehicle):
    def ride(self,color,type):
        self.color=color
        self.type=type
        print('the bike is ridden')
obc=car()
obc.start_engine('kia','S20')
obc.drive('white',4)
obb=bike()
obb.start_engine('swift','TSI')
obb.ride('red','FZ')