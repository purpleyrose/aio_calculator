from math_functions import arithmetic, functions, geometric_calculations, calculus, misc, sums

def math_mode():
    print("Which function would you like to use?")
    function = int(input("1. Arithmetic\n 2. Functions \n 3. Geometric Calculations \n 4. Calculus \n 5. Miscellaneous \n 6. Sums\n 7. Exit\n"))
    match function:
        case 1:
            arithmetic.arithmetic_main()
        case 2:
            functions.functions_main()
        case 3: 
            geometric_calculations.geometric_calculations_main()
        case 4:
            calculus.calculus_main()
        case 5:
            misc.misc_main()
        case 6:
            sums.sums_main()
        case 7:
            exit()
        case _:
            print("Invalid function")
            math_mode()
            
def physics_mode():
    TBD()

def chemistry_mode():
    TBD()

def biology_mode():
    TBD()

def ecology_mode():
    TBD()

def conversions_mode():
    TBD()

def everyday_life_mode():
    TBD()

def finance_mode():
    TBD()

def statistics_mode():
    TBD()


            
def TBD():
    print("This function is not yet implemented")
