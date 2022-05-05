
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length
        else:
            raise ValueError('Недопустимое значение длины')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError('Недопустимое значение ширины')

    def calculation_of_asphalt_mass(self, mass_one_square, thickness):
        print(int(self._length * self._width * mass_one_square * thickness / 1000), 'т.')


road = Road(length=20, width=5000)
road.calculation_of_asphalt_mass(25, 5)
