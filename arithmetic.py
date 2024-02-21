import math
import cmath


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
    if b == 0:
        return ZeroDivisionError

# Returns the floor of the quotient
def floor_division(a,b):
    return a // b

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

# Returns the nth root of a
def n_th_root(a, n):
    return a ** (1/n)

def absolute(a):
    return abs(a)

# ALlows for any real or complex number to be inputted
def factorial(a):
    return math.gamma(a)

# Uses complex log in the case that a or b is negative
def log(a, b):
    if a == 0:
        return "Undefined"
    if a > 0 or b > 0:
        return cmath.log(a, b)
    else:
        return math.log(a, b)

def ln(a):
    if a == 0:
        return "Undefined"
    if a > 0:
        return math.log(a, math.e)
    else:
        return cmath.log(a, math.e)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    if a == (math.pi/2) or a == (3*math.pi/2):
        return "Undefined"
    return math.tan(a)

# The following functions are all equivalent to the inverse of the above functions. 
def asin(a):
    if a < -1 or a > 1:
        return "Undefined"
    return math.asin(a)
def acos(a):
    if a < -1 or a > 1:
        return "Undefined"
    return math.acos(a)

def atan(a):
    return math.atan(a)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b) # The absolute value is used to prevent negative numbers from being returned

def radians_to_degrees(a):
    return math.degrees(a)

def degrees_to_radians(a):
    return math.radians(a)


def choice_operation(a, b):
    print("Which operation would you like to use?")
    operation = input(
        "+\t -\t x\t / \n //\t ^\t sqrt\t nrt \n |x|\t x!\t log\t ln \n Sin\t Cos\t Tan\n Asin\t Acos\t Atan\n gcd\t lcm\t radians degrees\n"
    )
    match operation:
        case "+":
            print(add(a, b))
        case "-":
            print(subtract(a, b))
        case "x":
            print(multiply(a, b))
        case "/":
            print(divide(a, b))
        case "//":
            print(floor_division(a, b))
        case "^":
            print(power(a, b))
        case "sqrt":
            print(square_root(a))
        case "nrt":
            print(n_th_root(a, b))
        case "|x|":
            print(absolute(a))
        case "x!":
            print(factorial(a))
        case "log":
            print(log(a, b))
        case "ln":
            print(ln(a))
        case "sin":
            print(sin(a))
        case "cos":
            print(cos(a))
        case "tan":
            print(tan(a))
        case "asin":
            print(asin(a))
        case "acos":
            print(acos(a))
        case "atan":
            print(atan(a))
        case "gcd":
            print(gcd(a, b))
        case "lcm":
            print(lcm(a, b))
        case "radians":
            print(radians_to_degrees(a))
        case "degrees":
            print(degrees_to_radians(a))
        case _:
            print("Invalid operation")

def arithmetic_main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    choice_operation(a, b)