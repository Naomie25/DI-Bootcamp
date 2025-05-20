import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be specified.")

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self.radius:.2f}, diameter: {self.diameter:.2f}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("Can only add Circle to Circle")

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __repr__(self):
        return f"Circle(radius={self.radius})"

c1 = Circle(radius=5)
c2 = Circle(diameter=12)

print(c1)  # Circle with radius: 5.00, diameter: 10.00
print(c2)  # Circle with radius: 6.00, diameter: 12.00
print("Area of c1:", c1.area())
print("Area of c2:", c2.area())

c3 = c1 + c2
print(c3)  # Circle with radius: 11.00, diameter: 22.00

print(c1 > c2)  # False
print(c1 < c2)  # True
print(c1 == c2) # False

circle_list = [c3, c1, c2]
circle_list.sort()
print(circle_list)  # Sorted by radius

