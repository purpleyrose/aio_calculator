import math
import cmath
from enum import Enum, auto
import matplotlib.pyplot as plt
import numpy as np

class FunctionType(Enum):
    LINEAR = auto()
    QUADRATIC = auto()
    CUBIC = auto()
    QUARTIC = auto()
    QUINTIC = auto()
    SEXTIC = auto()
    NTH_ROOT = auto()
    RATIONAL = auto()
    SINE = auto()
    COSINE = auto()
    EXPONENTIAL = auto()
    SQUARE_ROOT = auto()
    LN = auto()
    GAMMA = auto()
    
    
"""_summary_
    Allows mapping of several basic elementary functions.
    These functions include: a(k(x-d))+c, a(k(x-d))^2+c, a(k(x-d))^3+c, a(sin(k(x-d)))+c, a(cos(k(x-d)))+c
     a(e^(k(x-d)))+c, a*sqrt(k(x-d))+c  a*ln(k(x-d))+c, (a/kx-d)+c,  as well as the gamma function.
"""


class Function():
    def __init__(self, a, k, d, c, function_type):
        self.a = a
        self.k = k
        self.d = d
        self.c = c
        self.function_type = function_type
    
    def __str__(self):
        return f"{self.a}({self.k}(x-{self.d}))+{self.c}"

    def __repr__(self):
        return f"Function({self.a}, {self.k}, {self.d}, {self.c}, {self.function_type})"
    
    
    
    
    def evaluate(self, x):
        """_summary_
        Evaluates the function at a given x value.
        
        Args:
            x (float): The x value.
        
        Returns:
            float: The y value.
        
        Raises:
            ValueError: If the function type is invalid.
            TypeError: If x is not a floating point number.
        """
        match self.function_type:
            case FunctionType.LINEAR:
                return self.a*(self.k*(x-self.d))+self.c
            case FunctionType.QUADRATIC:
                return self.a*(self.k*(x-self.d))**2+self.c
            case FunctionType.CUBIC:
                return self.a*(self.k*(x-self.d))**3+self.c
            case FunctionType.QUARTIC:
                return self.a*(self.k*(x-self.d))**4+self.c
            case FunctionType.QUINTIC:
                return self.a*(self.k*(x-self.d))**5+self.c
            case FunctionType.SEXTIC:
                return self.a*(self.k*(x-self.d))**6+self.c
            case FunctionType.NTH_ROOT:
                return self.a*(self.k*(x-self.d))**(1/self.c)+self.c
            case FunctionType.RATIONAL:
                return self.a/(self.k*(x-self.d))+c
            case FunctionType.SINE:
                return self.a*(math.sin(self.k*(x-self.d)))+self.c
            case FunctionType.COSINE:
                return self.a*(math.cos(self.k*(x-self.d)))+self.c
            case FunctionType.EXPONENTIAL:
                return self.a*(math.e**(self.k*(x-self.d)))+self.c
            case FunctionType.SQUARE_ROOT:
                return self.a*(math.sqrt(self.k*(x-self.d)))+self.c
            case FunctionType.LN:
                return self.a*(math.log(self.k*(x-self.d)))+self.c
            case FunctionType.GAMMA:
                return self.a*(math.gamma(self.k*(x-self.d)))+self.c
            case _:
                raise ValueError("Invalid function type")
    def map(self, start=1, end=10, step=1):
        """_summary_
            Maps the function over a given range.
        Args:
            start (float): The initial x value.
            end (float): The final x value.
            step (float): The step size.
            
        Returns:
            dict: A dictionary containing the x and y values. The x values are the keys and the y values are the values.
            ex: {x1: y1, x2: y2, ...}
        
        Raises:
            ValueError: If the start value is greater than the end value.
            ValueError: If the step value is less than or equal to 0.
        """        
        
        if start > end:
            raise ValueError("Start value must be less than end value") 
        elif step <= 0:
            raise ValueError("Step value must be greater than 0")
        else:
            for x in np.arange(start, end, step):
                y = self.evaluate(x)
                print(f"(x:{x}, y:{y})")
    def plot(self, start=0, end=10, step=1):
        if start > end:
            raise ValueError("Start value mus tbe less than end value")
        elif step <= 0:
            raise ValueError("Step value must be greater than 0")
        else:
            for x in np.arange(start, end, step):
                y = self.evaluate(x)
                plt.plot(x, y, 'ro')
            plt.show()





def functions_main():
    mode = int(input("What do you want to do? \n\
        1. Evaluate a function \n\
        2. Map a function \n\
        3. Plot a function \n\
        4. Exit \n"))
    function_type = FunctionType(int(input("Enter the function type: 1. LINEAR, 2. QUADRATIC, 3. CUBIC, 4. QUARTIC, 5. QUINTIC, 6. SEXTIC, 7. NTH_ROOT, 8. RATIONAL, 9. SINE, 10. COSINE, 11. EXPONENTIAL, 12. SQUARE_ROOT, 13. LN, 14. GAMMA\n")))
    a = float(input("Enter the value of a: "))
    k = float(input("Enter the value of k: "))
    d = float(input("Enter the value of d: "))
    c = float(input("Enter the value of c: "))
    
    match mode:
        case 1:
            x = float(input("Enter the value of x: "))
            function = Function(a, k, d, c, function_type)
            print(function.evaluate(x))
        case 2:
            start = float(input("Enter the start value: "))
            end = float(input("Enter the end value: "))
            step = float(input("Enter the step value: "))
            function = Function(a, k, d, c, function_type)
            function.map(start, end, step)
        case 3:
            start = float(input("Enter the start value: "))
            end = float(input("Enter the end value: "))
            step = float(input("Enter the step value: "))
            function = Function(a, k, d, c, function_type)
            function.plot(start, end, step)
        case 4:
            return
        case _:
            raise ValueError("Invalid mode")