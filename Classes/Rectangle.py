class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self.__width = width

    def Area(self):
        return self._length * self.__width

    def __del__(self):
        print('Object Destruction initiated: ')

class Square(Rectangle):

    def Perimeter(self):
        return 4 * self._length

    def Area(self):
        return self._length ** 2

Shape = Rectangle(20, 15)
print("Area of rectangle: ",Shape.Area())
del Shape

Shape2 = Square(10, 10)
print("Area of square: ",Shape2.Area())
print("Perimeter of square: ",Shape2.Perimeter())
del Shape2