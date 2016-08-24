class Boat(object):
    def __init__(self):
        pass

    def swimm(self):
        print('I am swimming...')

class Car(object):
    __doc__ = '''Car factory'''
    def __init__(self, engine):
        self.engine = engine
        self.wheels = 4
        self.doors = 2

    def drive(self):
        print ('Driving far...')

    def stop(self):
        print('Pushing the brakes!')

class Van(Car, Boat):
    def __init__(self, wheels, weigh):
        super(self.__class__, self).__init__('diesel')
        self.wheels = wheels
        self.weigh = weigh

    @classmethod
    def get_heavy_van(cls, *args):
        return cls(2,4, *args)

volvo = Van.get_heavy_van()
print(volvo.__dict__)
print(Van.mro())
