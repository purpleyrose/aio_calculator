import math
import cmath


def divisible_by(a, b) -> bool:
    return a % b == 0

def fermat_little(a, p):
    return a ** (p - 1) % p == 1

def is_prime(n) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def prime_factors(n):   
    """_summary_
        A function to determine the prime factors of a given number n

    Args:
        n (int): The number to find the prime factors of

    Returns:
        list: A list of the prime factors of n
    """    
    factors = [] # Create an empty list to store the factors
    while n % 2 == 0: # If n is even, add 2 to the list of factors and divide n by 2, rounding down to the nearest integer
        factors.append(2) 
        n = n // 2
    for i in range(3, math.isqrt(n) + 1, 2): # For all odd numbers from 3 to the square root of n, rounded down to the nearest integer
        while n % i == 0: # If n is divisible by i, add i to the list of factors and divide n by i, rounding down to the nearest integer
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n) # If n is greater than 2, add n to the list of factors
    return factors

def quadractic_formula(a, b, c):
    """_summary_
        A function to solve the quadratic formula in the form ax^2 + bx + c = 0
    Args:
        a (float): The quadratic term
        b (float): The linear term in the quadratic equation
        c (float): The constant term in the quadratic equation
    """    
    discriminant = (b ** 2) - 4 * a * c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a) # We use cmath because the square root of a negative number is not defined in the real number system
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return x1, x2
    
def cubic_equation(a, b, c, d):
    """_summary_
        A function to solve the cubic equation in the form ax^3 + bx^2 + cx + d = 0
    Args:
        a (float): The cubic term
        b (float): The quadratic term
        c (float): The linear term
        d (float): The constant term
    """    
    q = (3 * a *c - (b ** 2))/(9 * (a ** 2))
    r = ((9 * a * b * c) - (27 * (a ** 2) * d) - (2 * (b ** 3))) / (54 * (a ** 3))
    S = math.cbrt(r * cmath.sqrt(q **3 + r ** 2)) # We use cmath because the square root of a negative number is not defined in the real number system
    T = math.cbrt(r - cmath.sqrt(q **3 + r ** 2))
    
    x1 = S + T - (b / (3 * a))
    x2 = -((S + T)/2) - (b / (3 * a)) + ((S - T) * (3 ** 0.5) * 0.5j)
    x3 = -((S + T)/2) - (b / (3 * a)) - ((S - T) * (3 ** 0.5) * 0.5j)
    return x1, x2, x3


def fibonaci_nth(n: int):
    """_summary_
        A function to find the nth number in the Fibonacci sequence
    Args:
        n (int): The position of the number in the Fibonacci sequence
    
    Returns:
        int: The nth number in the Fibonacci sequence
    
    Raises:
        ValueError: If n is less than 0
        TypeError: If n is not an integer
    """    
    try:
        golden = (1 + math.sqrt(5)) / 2 # The golden ratio, phi
        return math.floor((golden ** n - (-golden) ** -n) / math.sqrt(5)) # The formula for the F_nth number in the Fibonacci sequence is (phi^n - (-phi)^-n) / sqrt(5)
    except TypeError:
        raise TypeError("n must be an integer")
    except ValueError:
        raise ValueError("n must be greater than 0")

def twod_distance(x1, y1, x2, y2):
    """_summary_
        A function to find the distance between two points in a 2D plane
    Args:
        x1 (float): The x coordinate of the first point
        y1 (float): The y coordinate of the first point
        x2 (float): The x coordinate of the second point
        y2 (float): The y coordinate of the second point
    
    Returns:
        float: The distance between the two points
    """    
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def complex_to_polar(a, b):
    """_summary_
        A function to convert a complex number from rectangular form to polar form
    Args:
        a (float): The real part of the complex number
        b (float): The imaginary part of the complex number
    
    Returns:
        tuple: A tuple containing the magnitude and the angle of the complex number
    """    
    magnitude = math.sqrt(a ** 2 + b ** 2) # By the Pythagorean theorem
    angle = math.atan(b / a) # By the definition of the tangent ratio
    return magnitude, angle

def polar_to_cartesian(r, theta):
    """_summary_
        A function to convert a complex number from polar form to rectangular form
    Args:
        r (float): The magnitude of the complex number
        theta (float): The angle of the complex number
    
    Returns:
        tuple: A tuple containing the real and imaginary parts of the complex number
    """    
    a = r * math.cos(theta)
    b = r * math.sin(theta)
    return a, b



def misc_main():
    
    print("Which function would you like to use?")
    function = int(input("1. Divisible by\n 2. Fermat's Little Theorem \n 3. Is Prime \n 4. Prime Factors \n 5. Quadratic Formula \n 6. Cubic Equation \n 7. Fibonacci nth \n 8. 2D Distance \n 9. Complex to Polar \n 10. Polar to Cartesian \n 11. Exit\n"))
    match function:
        case 1:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            print(divisible_by(a, b))
        case 2:
            a = int(input("Enter the base: "))
            p = int(input("Enter the prime number: "))
            print(fermat_little(a, p))
        case 3:
            n = int(input("Enter the number: "))
            print(is_prime(n))
        case 4:
            n = int(input("Enter the number: "))
            print(prime_factors(n))
        case 5:
            a = int(input("Enter the quadratic term: "))
            b = int(input("Enter the linear term: "))
            c = int(input("Enter the constant term: "))
            print(quadractic_formula(a, b, c))
        case 6:
            a = int(input("Enter the cubic term: "))
            b = int(input("Enter the quadratic term: "))
            c = int(input("Enter the linear term: "))
            d = int(input("Enter the constant term: "))
            print(cubic_equation(a, b, c, d))
        case 7:
            n = int(input("Enter the position of the number in the Fibonacci sequence: "))
            print(fibonaci_nth(n))
        case 8:
            x1 = int(input("Enter the x coordinate of the first point: "))
            y1 = int(input("Enter the y coordinate of the first point: "))
            x2 = int(input("Enter the x coordinate of the second point: "))
            y2 = int(input("Enter the y coordinate of the second point: "))
            print(twod_distance(x1, y1, x2, y2))
        case 9:
            a = int(input("Enter the real part of the complex number: "))
            b = int(input("Enter the imaginary part of the complex number: "))
            print(complex_to_polar(a, b))
        case 10:
            r = int(input("Enter the magnitude of the complex number: "))
            theta = int(input("Enter the angle of the complex number: "))
            print(polar_to_cartesian(r, theta))
        case 11:
            exit()