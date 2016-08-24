class Car(object):
    __doc__ = '''Car factory'''
    def __init__(self, color='White'):
        self.color = color

    def __str__(self):
        return self.color * 2

mazda = Car()
print(dir(mazda))
