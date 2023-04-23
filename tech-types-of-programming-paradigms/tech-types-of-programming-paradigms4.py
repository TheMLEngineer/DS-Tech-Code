class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create a Circle object
circle = Circle(5)
print("Area of the circle:", circle.area())          # Output: Area of the circle: 78.5
print("Perimeter of the circle:", circle.perimeter()) # Output: Perimeter of the circle: 31.400000000000002
