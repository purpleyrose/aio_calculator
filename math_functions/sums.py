import math


class ArithmeticSequence:
    def __init__(self, a, d):
        self.a = a
        self.b = b
    
    def nth_term(self, n):
        return self.a + (n-1)*self.d

    def sum(self, n):
        return n/2*(self.a+self.nth_term(n))
    
    def map(self, n):
        for i in range(1, n+1):
            print(f"n: {i}, a: {self.nth_term(i)}, s: {self.sum(i)}")
    
    def to_nth_form(t_a, t_b):
        self.a = (t_a + t_b)/2
        self.d = t_b - t_a
        return self.a, self.d
    def finite_terms(t):
        """_summary_
        Returns the number of terms in the sequence
        Args:
            t (float): The last term in the sequence

        Returns:
            int: The number of terms in the sequence
        
        Raises:
            ValueError: If t is not a floating point number
        """        
        return (t - self.a)/self.d + 1
    
    def infinite_sum():
        """_summary_
        Returns the sum of an infinite sequence
        Returns:
            str: "Undefined"
        """        
        return "Undefined"


class GeometricSequence:
    def __init__(self, a, r):
        self.a = a
        self.r = r
    
    def nth_term(self, n):
        return self.a * self.r ** (n-1)

    def sum(self, n):
        return self.a * (1 - self.r ** n)/(1 - self.r)
    
    def map(self, n):
        for i in range(1, n+1):
            print(f"n: {i}, a: {self.nth_term(i)}, s: {self.sum(i)}")
    
    def to_nth_form(t_a, t_b):
        self.a = t_a
        self.r = t_b/t_a
        return self.a, self.r
    def finite_terms(t):
        """_summary_
        Returns the number of terms in the sequence
        Args:
            t (float): The last term in the sequence

        Returns:
            int: The number of terms in the sequence
        
        Raises:
            ValueError: If t is not a floating point number
        """        
        return math.log(t/self.a, self.r) + 1
    
    def infinite_sum():
        """_summary_
        Returns the sum of an infinite sequence
        Returns:
            str: "Undefined"
            float: self.a/(1-self.r), if abs(self.r) <= 1
        
        """        
        if math.abs(self.r) > 1:
            return "Undefined"
        else:
            return self.a/(1-self.r)


def collatz(n):
    """_summary_
        A function to return the stopping time of a given number n in the Collatz sequence.
    Args:
        n (int): The seed in the Collatz sequence
    
    Returns:
        int: The stopping time of the seed in the Collatz sequence
    
    Raises:
        ValueError: If n is not a positive integer
        TypeError: If n is not an integer
    """    
    steps = 0
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        steps += 1
    return steps


def sums_main():
    print("Which sequence would you like to use?")
    sequence = int(input(" 1. Arithmetic\n 2. Geometric\n 3. Collatz stopping time \n"))
    match sequence:
        case 1:
            print("What do you want to do with the sequence?")
            operation = int(input(" 1. Find the nth term\n 2. Find the sum of the first n terms\n 3. Map the sequence\n 4. Find a and r given two points \n 5. Find the number of terms"))
            match operation:
                case 1:
                    a = float(input("Enter the first term: "))
                    d = float(input("Enter the common difference: "))
                    n = int(input("Enter the term number: "))
                    seq = ArithmeticSequence(a, d)
                    print(f"The {n}th term is {seq.nth_term(n)}")
                case 2:
                    a = float(input("Enter the first term: "))
                    d = float(input("Enter the common difference: "))
                    n = int(input("Enter the number of terms: "))
                    seq = ArithmeticSequence(a, d)
                    print(f"The sum of the first {n} terms is {seq.sum(n)}")
                case 3:
                    a = float(input("Enter the first term: "))
                    d = float(input("Enter the common difference: "))
                    n = int(input("Enter the number of terms: "))
                    seq = ArithmeticSequence(a, d)
                    seq.map(n)
                case 4:
                    t_a = float(input("Enter the first term: "))
                    t_b = float(input("Enter the second term: "))
                    seq = ArithmeticSequence(a, d)
                    print(seq.to_nth_form(t_a, t_b))
                case 5:
                    a = float(input("Enter the first term: "))
                    d = float(input("Enter the common difference: "))
                    t = float(input("Enter the last term: "))
                    seq = ArithmeticSequence(a, d)
                    print(f"The number of terms is {seq.finite_terms(t)}")
        case 2:
            print("What do you want to do with the sequence?")
            operation = int(input(" 1. Find the nth term\n 2. Find the sum of the first n terms\n 3. Map the sequence\n 4. Find a and r given two points \n 5. Find the number of terms"))
            match operation:
                case 1:
                    a = float(input("Enter the first term: "))
                    r = float(input("Enter the common ratio: "))
                    n = int(input("Enter the term number: "))
                    seq = GeometricSequence(a, r)
                    print(f"The {n}th term is {seq.nth_term(n)}")
                case 2:
                    a = float(input("Enter the first term: "))
                    r = float(input("Enter the common ratio: "))
                    n = int(input("Enter the number of terms: "))
                    seq = GeometricSequence(a, r)
                    print(f"The sum of the first {n} terms is {seq.sum(n)}")
                case 3:
                    a = float(input("Enter the first term: "))
                    r = float(input("Enter the common ratio: "))
                    n = int(input("Enter the number of terms: "))
                    seq = GeometricSequence(a, r)
                    seq.map(n)
                case 4:
                    t_a = float(input("Enter the first term: "))
                    t_b = float(input("Enter the second term: "))
                    seq = GeometricSequence(a, r)
                    print(seq.to_nth_form(t_a, t_b))
                case 5:
                    a = float(input("Enter the first term: "))
                    r = float(input("Enter the common ratio: "))
                    t = float(input("Enter the last term: "))
                    seq = GeometricSequence(a, r)
                    print(f"The number of terms is {seq.finite_terms(t)}")
        case 3:
            n = int(input("Enter the seed: "))
            print(f"The stopping time of {n} is {collatz(n)}")
        case _:
            raise ValueError("Invalid sequence type")
    return

            