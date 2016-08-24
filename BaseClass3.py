class Car(object):
    number_of_calls = 0
    def __init__(self):
        pass

    @staticmethod
    def drive():
        Car.number_of_calls += 1
        print('Driving')

Car.drive()
Car.drive()
print(Car.number_of_calls)
# mazda = Car()
# print(mazda.__class__)
# mazda.__dict__['color'] = 'White'
# mazda.color = 'Brown'
# print(mazda.__dict__)
# print(dir(Car()))

@staticmethod
def drive():
    Car.number_of_calls += 1
    print('Driving')
