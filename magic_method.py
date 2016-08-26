class Car():
    def __init__(self, name, color='white'):
        self.color = color
        self.name = name
        print('Car {} created'.format(self.name))

    def __del__(self):
        print('Das Auto {} ist caput!'.format(self.name))

    def __repr__(self):
        return '{}'.format(self.name)

    def __str__(self):
        return '{} '.format(self.name) * 2

mazda = Car('mazda')
print(mazda)
