import arithmetic

def greeting():
    print("*********************************")
    print("Hello! This is a simple calculator with several different functions, such as simple arithmatics, discrete sums, and mapping basic functions")

def choice_mode():
    print("Which mode would you like to use?")
    mode = int(input("1. Simple arithmetics\n 2. Discrete sums\n 3. Mapping basic functions\n 4. Geometric Calculations\n 5: Exit"))
    match mode:
        case 1:
            arithmetic.arithmatics_main()
        case 2:
            TBD()
            #discrete_sums_main()
        case 3: 
            TBD()
            #mapping_basic_functions_main()
        case 4:
            TBD()
            #geometric_calculations_main()
        case 5:
            print("Exiting...")
            exit()


def TBD():
    print("This function is not yet implemented")


def main():
    greeting()
    choice_mode()

if __name__=="__main__":
    main()
