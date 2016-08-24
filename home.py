class Engine(object):
    num = 0
    def __init__(self):
        Engine.num += 1
        if Engine.num % 3 == 0:
            self.type_of_engine = 'diesel'
            self.consumption = 6
            self.cost = 1.8
        else:
            self.type_of_engine = 'benzin'
            self.consumption = 8
            self.cost= 2.4
        if Engine.num % 5 == 0:
            self.tank = 75
        else:
            self.tank = 60

class Car(Engine):
    def __init__(self, color='White'):
        super(self.__class__, self).__init__()
        self.color = color
        self.cost = 10000
        self.max_distance_benz = 200000
        self.max_distance_benz = 150000
        self.price_diesel = 1.8
        self.price_benzin = 2.4




car_pool =(Car() for i in xrange(30))
for i in car_pool:
    print(i.__dict__)
# for i in xrange(30):
#     mazda = Car()
#     print(mazda.__dict__)
