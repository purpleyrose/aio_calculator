import math
import cmath
"""_summary_
    Allows mapping of several basic elementary functions.
    These functions include: a(k(x-d))+c, a(k(x-d))^2+c, a(k(x-d))^3+c, a(sin(k(x-d)))+c, a(cos(k(x-d)))+c
     a(e^(k(x-d)))+c, a*sqrt(k(x-d))+c  a*ln(k(x-d))+c, as well as the gamma function.
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
        """
        if self.function_type == "linear": # y = ax + b
            return self.a*self.k*(x-self.d)+self.c
        elif self.function_type == "quadratic": # y = a(k(x-d))^2+c 
            return self.a*self.k*(x-self.d)**2+self.c
        elif self.function_type == "cubic":
            return self.a*self.k*(x-self.d)**3+self.c # y = a(k(x-d))^3+c 
        elif self.function_type == "sine":
            return self.a*math.sin(self.k*(x-self.d))+self.c # y = a(sin(k(x-d)))+c where x is in radians
        elif self.function_type == "cosine":
            return self.a*math.cos(self.k*(x-self.d))+self.c # y = a(cos(k(x-d)))+c where x is in radians
        elif self.function_type == "exponential":
            return self.a*math.e**(self.k*(x-self.d))+self.c # y = a(e^(k(x-d)))+c 
        elif self.function_type == "square root":
            return self.a*math.sqrt(self.k*(x-self.d))+self.c # y = a*sqrt(k(x-d))+c 
        elif self.function_type == "ln":
            return self.a*math.log(self.k*(x-self.d))+self.c # y = a*ln(k(x-d))+c, where k > 0, x >= 0
        elif self.function_type == "gamma":
            return math.gamma(x) # y = gamma(x) x != Z- (x is not a negative integer)
        else:
            raise ValueError("Invalid function type")
    
    def map(self, start, end, step):
        """_summary_
            Maps the function over a given range.
        Args:
            start (float): The inital x value.
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
            for x in range(start, end, step):
                y = self.evaluate(x)
                print(f"(x:{x}, y:{y})")
    


