class Point:

    class_attribute = "Should be treated as constant of global config for all classes"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"draw ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
print(point.draw())
print(Point.class_attribute)
point = Point.zero()
print(point.draw())


class Magic1:

    def __init__(self):
        pass


class Magic2:

    def __init__(self):
        pass

    def __str__(self):
        return "override string print out"


magic1 = Magic1()
magic2 = Magic2()
print(magic1)
print(magic2)
