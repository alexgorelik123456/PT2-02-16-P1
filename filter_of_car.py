from pprint import *
ENG_TYPE_GASOLINE = 'gasoline'
ENG_TYPE_DIESEL = 'diesel'

class Car():
    car_pool=[]
    def __init__(self, eng_type, cost, mileage):
        self.eng_type = eng_type
        self.cost = cost
        self.mileage = mileage
        Car.car_pool.append(self)

    def __repr__(self):
        return ', '.join(str(self.__dict__[_]) for _ in self.__dict__)

Car(ENG_TYPE_DIESEL, 100, 400)
Car(ENG_TYPE_DIESEL, 150, 200)
Car(ENG_TYPE_DIESEL, 180, 100)
Car(ENG_TYPE_GASOLINE, 200, 1400)
Car(ENG_TYPE_GASOLINE, 180, 1200)
Car(ENG_TYPE_GASOLINE, 80, 1200)
p(Car.car_pool)
diesels = filter(lambda x: x.engine_type == ENG_TYPE_DIESEL, Car.car_pool)
p(diesels)
