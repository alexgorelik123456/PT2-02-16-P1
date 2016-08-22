# class Animals:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def say(self):
#         print(self.name)
#         print(self.color)
#
# mouse = Animals(name='Jerry', color='Brown')
# mouse2 = Animals(name='Berry', color='Gray')
# print(dir(mouse))
# print(mouse.__dict__)
#
# mouse.say()
# mouse2.say()
#
# class Mice(object):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def say(self):
#         print(self.name, self.color)
#
# mouse = Mice(name='Jerry', color='Brown')
# print(dir(mouse))
# print(mouse.__dict__)
# mouse.say()

def flash():
    print('Flashing my lights')

class Car(object):
    recalled = None
    def __init__(self, doors, color, consumption=1, wheels=4, feature=None):
        self.wheels = wheels
        self.__color = color
        self.doors = doors
        self.consumption = consumption
        self.tank = 90
        self.feature = feature
        if self.feature:
            self.feature()

    @property
    def see_tank(self):
        if self.tank > 90:
            print('Take to service and replace tank to bigger')
        return self.tank

    @see_tank.setter
    def see_tank(self, new_value):
        if new_value > self.tank:
            print('flows out!')
            return
        self.tank = new_value

    #def auto(self):
    #   print(self.wheels, self.color, self.doors)

    def ride(self, hours=10):
        self.tank = self.tank - hours
        print('my color {}'.format(self.__color))
        if Car.recalled:
            print('Blablabla')
            return
        print('Left {} hours to drive'.format(self.tank))
        self.doors = 'closed'
        print('Doors closed, riding')
        self.tank = self.tank - hours * self.consumption
        print('Stopped {} hours left'.format(self.tank))

mazda = Car('opened', 'white', feature=flash)
print(mazda.see_tank)
mazda.ride()
mazda.see_tank=100
print(mazda.see_tank)

#print(mazda.__dict__)

# Car.recalled = True
# mazda.ride()




