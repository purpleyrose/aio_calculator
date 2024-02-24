from math_functions import arithmetic, functions, geometric_calculations
import modes
def greeting():
    print("*********************************")
    print("Hello! This is a simple calculator with several different functions, such as simple arithmetics, discrete sums, and mapping basic functions")

def choice_mode():
    print("Which mode would you like to use?")
    mode = int(input(" 1. Math\n 2. Physics \n 3. Chemistry \n 4. Biology \n 5.Ecology \n 6.Conversions \n 7. Everyday life\n 8. Finance\n 9. Statistics\n 10. Exit\n"))
    match mode:
        case 1:
            modes.math_mode()
        case 2:
            modes.physics_mode()
        case 3:
            modes.chemistry_mode()
        case 4:
            modes.biology_mode()
        case 5:
            modes.ecology_mode()
        case 6:
            modes.conversions_mode()
        case 7:
            modes.everyday_life_mode()
        case 8:
            modes.finance_mode()
        case 9:
            modes.statistics_mode()
        case 10:
            exit()
        case _:
            print("Invalid mode")
            choice_mode()      
            




def main():
    greeting()
    choice_mode()

if __name__=="__main__":
    main()
