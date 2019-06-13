#
# Example file for working with classes

# Notes on super() in single and multiple inheritance hierarchies: https://realpython.com/python-super/
#


class MyClass:
    def __init__(self, name="default"):
        self.name = name

    @staticmethod
    def method1(some_string="No string provided."):
        print("MyClass method1 is a static method. " + some_string)

    def method2(self):
        print("MyClass method2 is an instance method with name = " + self.name)

    @classmethod
    def method3(cls):
        print("MyClass method3 is a class method. It can call static methods.")
        cls.method1()


class MySubClass(MyClass):
    def __init__(self, age=100):
        super().__init__()
        self.age = age

    @staticmethod
    def method1(some_string="No string provided."):
        print("MySubClass method1 is a static method. " + some_string)
        super(MySubClass, MySubClass).method1(some_string)

    def method2(self):
        print("MySubClass instance has age = " + str(self.age) + " and name = " + self.name)


class Rectangle:
    def __init__(self, length, width):
        print("Instantiating: class Rectangle")
        self.length = length
        self.width = width

    def area(self):
        print("Calculating area from class Rectangle")
        return self.length * self.width

    def perimeter(self):
        print("Calculating perimeter from class Rectangle")
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        print("Instantiating: class Square")
        super(Square, self).__init__(length, length)


class Cube(Square):
    def __init__(self, length):
        print("Instantiating: class Cube")
        super(Cube, self).__init__(length)

    def surface_area(self):
        print("Calculating surface area from class Cube")
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        print("Calculating volume from class Cube")
        face_area = super(Square, self).area()
        return face_area * self.length


class Triangle:
    def __init__(self, base, height):
        print("Instantiating: class Triangle")
        self.base = base
        self.height = height

    def area(self):
        print("Calculating area from class Triangle")
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        print("Instantiating: class RightPyramid")
        self.base = base
        self.slant_height = slant_height
        print(RightPyramid.__mro__)
        super(RightPyramid, self).__init__(self.base)

    def area(self):
        print("Calculating area from class RightPyramid")
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


def main():
    c1 = MyClass()
    c2 = MyClass("John")
    c1.method1("This is a string")

    c1.method2()
    c2.method2()

    c1.method3()

    sc1 = MySubClass()
    sc1.method1()
    sc1.method2()

    cube = Cube(3)
    print(cube.volume())
    print(cube.surface_area())

    pyramid = RightPyramid(2, 4)
    print(pyramid.area())
    print(pyramid.perimeter())


if __name__ == "__main__":
    main()
