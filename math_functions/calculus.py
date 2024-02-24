import math
from math_functions import functions as fun


class Derivative(fun.Function):
    def __init__(self, a, k, d, c, function_type):
        super().__init__(a, k, d, c, function_type)
    
    def __str__(self):
        return f"Derivative of {super().__str__()}"
    
    def evaluate(self, x):
        match self.function_type:
            case fun.FunctionType.LINEAR:
                return self.a*self.k
            case fun.FunctionType.QUADRATIC:
                return 2*self.a*self.k*(x-self.d)
            case fun.FunctionType.CUBIC:
                return 3*self.a*self.k*(x-self.d)**2
            case fun.FunctionType.QUARTIC:
                return 4*self.a*self.k*(x-self.d)**3
            case fun.FunctionType.QUINTIC:
                return 5*self.a*self.k*(x-self.d)**4
            case fun.FunctionType.SEXTIC:
                return 6*self.a*self.k*(x-self.d)**5
            case fun.FunctionType.RATIONAL:
                return -self.a/(self.k*(x-self.d))**2
            case fun.FunctionType.SINE:
                return self.a*self.k*math.cos(self.k*(x-self.d))
            case fun.FunctionType.COSINE:
                return -self.a*self.k*math.sin(self.k*(x-self.d))
            case fun.FunctionType.EXPONENTIAL:
                return self.a*self.k*math.e**(self.k*(x-self.d))
            case fun.FunctionType.SQUARE_ROOT:
                return self.a*self.k/(2*math.sqrt(self.k*(x-self.d)))
            case fun.FunctionType.LN:
                return self.a*self.k/(self.k*(x-self.d))
            case fun.FunctionType.GAMMA:
                raise ValueError("The derivative of the gamma function is not yet implemented")
            case _:
                raise ValueError("The derivative of this function is not yet implemented")
        
    def map(self, start=1, end=10, step=1, show_original=False):
        """_summary_
            Maps the derivative of the function over a given range.
        Args:
            start (float): The initial x value.
            end (float): The final x value.
            step (float): The step size.
            show_original (bool): Whether to print the original function values as well.
            
        Returns:
            dict: A dictionary containing the x values as keys and the corresponding y values as values.

        Raises:
            ValueError: If the function type is not valid.
            ValueError: If the derivative of the gamma function is requested.
            ValueError: If start > end.
            ValueError: If step <= 0.
        """
        
        try:
            match show_original:
                case True:
                    for x in range(start, end, step):
                        y = self.evaluate(x)
                        print(f"x: {x}, y: {y}, original: x: {x}, y: {super().evaluate(x)}")
                case False:
                    for x in range(start, end, step):
                        y = self.evaluate(x)
                        print(f"x: {x}, y: {y}")
        except ValueError as e:
            print(e)
                        

Derivative(1, 2, 3, 4, fun.FunctionType.QUADRATIC).map(1, 10, 1, True)
                

                
class Integral(fun.Function):
    def __init__(self, a, k, d, c, function_type):
        super().__init__(a, k, d, c, function_type)
    
    def __str__(self):
        return f"Integral of {super().__str__()}"
    
    def evaluate(self, upper_bound, lower_bound):
        match self.function_type:
            case fun.FunctionType.LINEAR:
                return self.a*self.k*(upper_bound-self.d)+self.c-(self.a*self.k*(lower_bound-self.d)+self.c)
            case fun.FunctionType.QUADRATIC:
                return (self.a*self.k*(upper_bound-self.d)**2+self.c)-(self.a*self.k*(lower_bound-self.d)**2+self.c)
            case fun.FunctionType.CUBIC:
                return (self.a*self.k*(upper_bound-self.d)**3+self.c)-(self.a*self.k*(lower_bound-self.d)**3+self.c)
            case fun.FunctionType.QUARTIC:
                return (self.a*self.k*(upper_bound-self.d)**4+self.c)-(self.a*self.k*(lower_bound-self.d)**4+self.c)
            case fun.FunctionType.QUINTIC:
                return (self.a*self.k*(upper_bound-self.d)**5+self.c)-(self.a*self.k*(lower_bound-self.d)**5+self.c)
            case fun.FunctionType.SEXTIC:
                return (self.a*self.k*(upper_bound-self.d)**6+self.c)-(self.a*self.k*(lower_bound-self.d)**6+self.c)
            case fun.FunctionType.RATIONAL:
                return self.a*math.log(self.k*(upper_bound-self.d))+self.c-(self.a*math.log(self.k*(lower_bound-self.d))+self.c)
            case fun.FunctionType.SINE:
                return -self.a*math.cos(self.k*(upper_bound-self.d))+self.c-(-self.a*math.cos(self.k*(lower_bound-self.d))+self.c)
            case fun.FunctionType.COSINE:
                return self.a*math.sin(self.k*(upper_bound-self.d))+self.c-(self.a*math.sin(self.k*(lower_bound-self.d))+self.c)
            case fun.FunctionType.EXPONENTIAL:
                return self.a*math.e**(self.k*(upper_bound-self.d))+self.c-(self.a*math.e**(self.k*(lower_bound-self.d))+self.c)
            case fun.FunctionType.SQUARE_ROOT:
                return self.a*(2/3)*math.sqrt(self.k*(upper_bound-self.d))+self.c-(self.a*(2/3)*math.sqrt(self.k*(lower_bound-self.d))+self.c)
            case fun.FunctionType.LN:
                return self.a*(upper_bound-self.d)*math.log(self.k*(upper_bound-self.d))+self.c-(self.a*(lower_bound-self.d)*math.log(self.k*(lower_bound-self.d))+self.c)
            case fun.FunctionType.GAMMA:
                raise ValueError("The integral of the gamma function is not yet implemented")
            case _:
                raise ValueError("The integral of this function is not yet implemented")

    def map(self, start=1, end=10, step=1):
        """_summary_
            Maps the antiderivative of the function over a given range.
            
        Args:
            start (float): The initial x value.
            end (float): The final x value.
            step (float): The step size.
        
        Returns:
            dict: A dictionary containing the x values as keys and the corresponding y values as values.
        
        Raises:
            ValueError: If the function type is not valid.
            ValueError: If the integral of the gamma function is requested.
            ValueError: If start > end.
            ValueError: If step <= 0.
        """
            
        if start > end:
            raise ValueError("The start value must be less than the end value")
        elif step <= 0:
            raise ValueError("The step size must be greater than 0")
        else:
            for x in range(start, end, step):
                y = self.evaluate(x, start)
                print(f"x: {x}, y: {y}")
                
    
def calculus_main():
    print("Which function would you like to use?")
    function = int(input(" 1. Derivative\n 2. Integral\n"))
    match function:
        case 1:
            print("Would you like to map the function, or evaluate it at a specific point?")
            operation = int(input(" 1. Map\n 2. Evaluate\n"))
            match operation:
                case 1:
                    print("Which function type would you like to use?")
                    function_type = int(input("1. Linear\n 2. Quadratic\n 3. Cubic\n 4. Quartic\n 5. Quintic\n 6. Sextic\n 7. Rational\n 8. Sine\n 9. Cosine\n 10. Exponential\n 11. Square Root\n 12. Natural Logarithm\n 13. Gamma\n"))
                    a = float(input("Enter the value of a: "))
                    k = float(input("Enter the value of k: "))
                    d = float(input("Enter the value of d: "))
                    c = float(input("Enter the value of c: "))
                    show_original = input("Would you like to show the original function values as well? (y/n)")
                    match show_original:
                        case "y":
                            Derivative(a, k, d, c, fun.FunctionType(function_type)).map(show_original=True)
                        case "n":
                            Derivative(a, k, d, c, fun.FunctionType(function_type)).map()
                case 2:
                    print("Which function type would you like to use?")
                    function_type = int(input("1. Linear\n 2. Quadratic\n 3. Cubic\n 4. Quartic\n 5. Quintic\n 6. Sextic\n 7. Rational\n 8. Sine\n 9. Cosine\n 10. Exponential\n 11. Square Root\n 12. Natural Logarithm\n 13. Gamma\n"))
                    a = float(input("Enter the value of a: "))
                    k = float(input("Enter the value of k: "))
                    d = float(input("Enter the value of d: "))
                    c = float(input("Enter the value of c: "))
                    x = float(input("Enter the value of x: "))
                    print(Derivative(a, k, d, c, fun.FunctionType(function_type)).evaluate(x))
        case 2:
            print("Which function type would you like to use?")
            function_type = int(input(" 1. Linear\n 2. Quadratic\n 3. Cubic\n 4. Quartic\n 5. Quintic\n 6. Sextic\n 7. Rational\n 8. Sine\n 9. Cosine\n 10. Exponential\n 11. Square Root\n 12. Natural Logarithm\n 13. Gamma\n"))
            a = float(input("Enter the value of a: "))
            k = float(input("Enter the value of k: "))
            d = float(input("Enter the value of d: "))
            c = float(input("Enter the value of c: "))
            upper_bound = float(input("Enter the upper bound: "))
            lower_bound = float(input("Enter the lower bound: "))
            Integral(a, k, d, c, fun.FunctionType(function_type)).evaluate(upper_bound, lower_bound)
        case _:
            raise ValueError("Invalid function type")


