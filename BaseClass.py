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

class Car(object):
    recalled = None
    def __init__(self, doors, color, consumption=1, wheels=4):
        self.wheels = wheels
        self.color = color
        self.doors = doors
        self.consumption = consumption
        self.tank = 90

    def auto(self):
        print(self.wheels, self.color, self.doors)

    def ride(self, hours=10):
        if Car.recalled:
            print('Blablabla')
            return
        print('Left {} hours to drive'.format(self.tank))
        self.doors = 'closed'
        print('Doors closed, riding')
        self.tank = self.tank - hours * self.consumption
        print('Stopped {} hours left'.format(self.tank))

mazda = Car('opened', 'white')
toyota = Car('opened', 'red')
mazda.ride()
toyota.ride()

# Car.recalled = True
# mazda.ride()




