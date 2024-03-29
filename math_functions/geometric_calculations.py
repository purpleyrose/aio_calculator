import math



class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2) # By area of a circle = pi * r^2

    def circumference(self):
        return 2 * math.pi * self.radius # Circumference = 2 pi r
    
    def diameter(self):
        return 2 * self.radius
    
    def sector_area(self, angle):
        return (angle/360) * math.pi * (self.radius ** 2)
    
    def arc_length(self, angle):
        return (angle/360) * 2 * math.pi * self.radius
    

class Triangle:
    def __init__(self, a, b, c, A, B, C):
        self.a = a
        self.b = b
        self.c = c
        self.A = A
        self.B = B
        self.C = C
    

    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        """_summary_
        Herons formula for area of a triangle states that area is equal to sqrt(s(s-a)(s-b)(s-c)), where s is the semiperimeter (the perimeter divided by two) of the triangle
        Returns:
            float: The result may be positive real number
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    
   
    def pythagorean_theorem(self):
        return math.sqrt((self.a ** 2) + (self.b ** 2)) # By the pythagorean theorem; a^2+b^2=c^2
    


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def diagonal(self):
        return math.sqrt((self.length ** 2) + (self.width ** 2))
    
    def is_square(self):
        """[summary]
        Determines whether the given rectangle object is a square
        Returns:
            bool: Returns true if self.width is equal to self.length
        """        
        return self.length == self.width


class Polygon:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length
    def perimeter(self):
        return self.sides * self.length
    
    def area(self):
        return (1/2) * self.sides * self.length * self.apothem()
    
    def apothem(self):
        return self.length / (2 * math.tan(math.pi / self.sides))
    

class Sphere:
    def __init__(self, radius):
        self.radius = radius
    
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)
    
    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def volume(self):
        return math.pi * (self.radius ** 2) * self.height
    
    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def volume(self):
        return (1/3) * math.pi * (self.radius ** 2) * self.height
    
    def surface_area(self):
        return math.pi * self.radius * (self.radius + math.sqrt((self.height ** 2) + (self.radius ** 2)))

class Prism:
    def __init__(self, base, height, sides, width):
        self.base = base
        self.height = height
        self.width = width
        self.sides = sides
    
    def volume(self):
        return self.base * self.height * self.width
    
    def surface_area(self):
        return (2 * self.base) + (self.sides * self.height) + (self.sides * self.base)

class Pyramid:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def volume(self):
        return (1/3) * self.base * self.height
    
    def surface_area(self):
        return self.base + (1/2) * (self.base * self.height)

class Parallelogram:
    def __init__(self, base, height, side):
        self.base = base
        self.height = height
        self.side = side
    
    def area(self):
        return self.base * self.height
    
    def perimeter(self):
        return 2 * (self.base + self.side)
    
    def diagonal(self):
        return math.sqrt((self.base ** 2) + (self.height ** 2))

class Rhombus:
    def __init__(self, base, height, side):
        self.base = base
        self.height = height
        self.side = side
    
    def area(self):
        return self.base * self.height
    
    def perimeter(self):
        return 4 * self.side
    
    def diagonal(self):
        return math.sqrt((self.base ** 2) + (self.height ** 2))

class Trapezoid:
    def __init__(self, base1, base2, height, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self):
        return (1/2) * (self.base1 + self.base2) * self.height
    
    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2
    
    def median(self):
        return (self.base1 + self.base2) / 2
    
    def height(self):
        return math.sqrt((self.side1 ** 2) - (((self.base2 - self.base1) ** 2) / 4))


class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return math.pi * self.a * self.b
    
    def circumference(self):
        return math.pi * (3 * (self.a + self.b) - math.sqrt((3 * self.a + self.b) * (self.a + 3 * self.b)))


def get_float_input(prompt):
    """_summary_
        Gets a float number from the user
    Args:
        prompt (str): The string that is displayed to the user to get the number

    Raises:
        TypeError: If the inputted number is not a float type.
    Returns:
        float: Returns a float number 
    
    """    
    while True:
        try:
            return float(input(prompt))
        except TypeError:
            print("Invalid number")



def geometric_calculations_main():
    print("Which shape would you like to calculate? ")
    shape = input("Circle\t Triangle\t Rectangle\t Polygon\t Sphere\t Cylinder\t Cone\t Prism\t Pyramid\t Parallelogram\t Rhombus\t Trapezoid\t Ellipse\n")

    match shape.lower():
        case "circle":
            radius = get_float_input("What is the radius of the circle? ")
            circle = Circle(radius)
            print("What would you like to calculate? ")
            calculation = input("Area\t Circumference\t Diameter\t Sector Area\t Arc Length\n")
            match calculation.lower():
                case "area":
                    print(circle.area())
                case "circumference":
                    print(circle.circumference())
                case "diameter":
                    print(circle.diameter())
                case "sector area":
                    angle = get_float_input("What is the angle of the sector? ")
                    print(circle.sector_area(angle))
                case "arc length":
                    angle = get_float_input("What is the angle of the arc? ")
                    print(circle.arc_length(angle))
                case _:
                    print("Invalid input")
        case "triangle":
            a = get_float_input("What is the length of side a? ")
            b = get_float_input("What is the length of side b? ")
            c = get_float_input("What is the length of side c? ")
            A = get_float_input("What is the angle of A (in radians)? If you do not know the length, put 0: ")
            B = get_float_input("What is the angle of B (in radians) ? If you do not know the length, put 0: ")
            C = get_float_input("What is the angle of C (in radians) ? If you do not know the length, put 0: ")
            triangle = Triangle(a, b, c, A, B, C)
            print("What would you like to calculate?")
            calculation = input("Perimeter\t Area\t Pythagorean Theorem\n")
            match calculation.lower():
                case "perimeter":
                    print(triangle.perimeter())
                case "area":
                    print(triangle.area())
                case "pythagorean theorem":
                    print(triangle.pythagorean_theorem())
                case _:
                    print("Invalid input")
        case "rectangle":
            length = get_float_input("What is the length of the rectangle? ")
            width = get_float_input("What is the width of the rectangle? ")
            rectangle = Rectangle(length, width)
            print("What would you like to calculate? ")
            calculation = input("Area\t Perimeter\t Diagonal\t Is Square\n")
            match calculation.lower():
                case "area":
                    print(rectangle.area())
                case "perimeter":
                    print(rectangle.perimeter())
                case "diagonal":
                    print(rectangle.diagonal())
                case "is square":
                    print(rectangle.is_square())
                case _:
                    print("Invalid input")
        case "polygon":
            sides = int(input("How many sides does the polygon have? "))
            length = get_float_input("What is the length of the polygon? ")
            polygon = Polygon(sides, length)
            print("What would you like to calculate? ")
            calculation = input("Perimeter\t Area\t Apothem\n")
            match calculation.lower():
                case "perimeter":
                    print(polygon.perimeter())
                case "area":
                    print(polygon.area())
                case "apothem":
                    print(polygon.apothem())
                case _:
                    print("Invalid input")
        case "sphere":
            radius = get_float_input("What is the radius of the sphere? ")
            sphere = Sphere(radius)
            print("What would you like to calculate? ")
            calculation = input("Volume\t Surface Area\n")
            match calculation.lower():
                case "volume":
                    print(sphere.volume())
                case "surface area":
                    print(sphere.surface_area())
                case _:
                    print("Invalid input")
        case "cylinder":
            radius = get_float_input("What is the radius of the cylinder? ")
            height = get_float_input("What is the height of the cylinder? ")
            cylinder = Cylinder(radius, height)
            print("What would you like to calculate? ")
            calculation = input("Volume\t Surface Area\n")
            match calculation.lower():
                case "volume":
                    print(cylinder.volume())
                case "surface area":
                    print(cylinder.surface_area())
                case _:
                    print("Invalid input")
        case "cone":
            radius = get_float_input("What is the radius of the cone? ")
            height = get_float_input("What is the height of the cone? ")
            cone = Cone(radius, height)
            print("What would you like to calculate?")
            calculation = input("Volume\t Surface Area\n")
            match calculation.lower():
                case "volume":
                    print(cone.volume())
                case "surface area":
                    print(cone.surface_area())
                case _:
                    print("Invalid input")
        case "prism":
            base = get_float_input("What is the base of the prism? ")
            height = get_float_input("What is the height of the prism? ")
            sides = get_float_input("How many sides does the prism have? ")
            prism = Prism(base, height, sides)
            print("What would you like to calculate?")
            calculation = input("Volume\t Surface Area\n")
            match calculation.lower():
                case "volume":
                    print(prism.volume())
                case "surface area":
                    print(prism.surface_area())
                case _:
                    print("Invalid input")
        case "pyramid":
            base = get_float_input("What is the base of the pyramid? ")
            height = get_float_input("What is the height of the pyramid? ")
            pyramid = Pyramid(base, height)
            print("What would you like to calculate?")
            calculation = input("Volume\t Surface Area\n")
            match calculation.lower():
                case "volume":
                    print(pyramid.volume())
                case "surface area":
                    print(pyramid.surface_area())
                case _:
                    print("Invalid input")
        case "parallelogram":
            base = get_float_input("What is the base of the parallelogram? ")
            height = get_float_input("What is the height of the parallelogram? ")
            side = get_float_input("What is the side of the parallelogram? ")
            parallelogram = Parallelogram(base, height, side)
            print("What would you like to calculate?")
            calculation = input("Area\t Perimeter\t Diagonal\n")
            match calculation.lower():
                case "area":
                    print(parallelogram.area())
                case "perimeter":
                    print(parallelogram.perimeter())
                case "diagonal":
                    print(parallelogram.diagonal())
                case _:
                    print("Invalid input")
        case "rhombus":
            base = get_float_input("What is the base of the rhombus? ")
            height = get_float_input("What is the height of the rhombus? ")
            side = get_float_input("What is the side of the rhombus? ")
            rhombus = Rhombus(base, height, side)
            print("What would you like to calculate?")
            calculation = input("Area\t Perimeter\t Diagonal\n")
            match calculation.lower():
                case "area":
                    print(rhombus.area())
                case "perimeter":
                    print(rhombus.perimeter())
                case "diagonal":
                    print(rhombus.diagonal())
                case _:
                    print("Invalid input")
        case "trapezoid":
            base1 = get_float_input("What is the length of the first base? ")
            base2 = get_float_input("What is the length of the second base? ")
            height = get_float_input("What is the height of the trapezoid? ")
            side1 = get_float_input("What is the length of the first side? ")
            side2 = get_float_input("What is the length of the second side? ")
            trapezoid = Trapezoid(base1, base2, height, side1, side2)
            print("What would you like to calculate?")
            calculation = input("Area\t Perimeter\t Median\t Height\n")
            match calculation.lower():
                case "area":
                    print(trapezoid.area())
                case "perimeter":
                    print(trapezoid.perimeter())
                case "median":
                    print(trapezoid.median())
                case "height":
                    print(trapezoid.height())
                case _:
                    print("Invalid input")
        case "ellipse":
            a = get_float_input("What is the length of a? ")
            b = get_float_input("What is the length of b? ")
            ellipse = Ellipse(a, b)
            print("What would you like to calculate? ")
            calculation = input("Area\t Circumference\n")
            match calculation.lower():
                case "area":
                    print(ellipse.area())
                case "circumference":
                    print(ellipse.circumference())
                case _:
                    print("Invalid input")
        case _:
            print("Invalid input")

