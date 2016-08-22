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

class Mice(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say(self):
        print(self.name, self.color)

mouse = Mice(name='Jerry', color='Brown')
print(dir(mouse))
print(mouse.__dict__)
mouse.say()
