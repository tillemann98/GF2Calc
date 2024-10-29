import locale
import math
import numpy as np

def calc_values_from_mikro(val1,datatype):
    rval1 = val1
    rval2 = format(val1/1000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval3 = format(val1/1000000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval4 = format(val1/1000000000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval5 = format(val1/1000000000000, ",").replace(".","%").replace(",",".").replace("%",",")
    print(rval1,"µ",datatype)
    print(rval2,"m",datatype)
    print(rval3,datatype)
    print(rval4,"k",datatype)
    print(rval5,"M",datatype)





def calc_values_from_mili(val1,datatype):
    rval1 = format(val1*1000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval2 = val1
    rval3 = format(val1/1000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval4 = format(val1/1000000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval5 = format(val1/1000000000, ",").replace(".","%").replace(",",".").replace("%",",")
    print(rval1,"µ",datatype)
    print(rval2,"m",datatype)
    print(rval3,datatype)
    print(rval4,"k",datatype)
    print(rval5,"M",datatype)






def calc_values_from_actual(val1,datatype):
    rval1 = format(val1*1000000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval2 = format(val1*1000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval3 = val1
    rval4 = format(val1/1000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval5 = format(val1/1000000, ",").replace(".","%").replace(",",".").replace("%",",")
    print(rval1,"µ",datatype)
    print(rval2,"m",datatype)
    print(rval3,datatype)
    print(rval4,"k",datatype)
    print(rval5,"M",datatype)





def calc_values_from_kilo(val1,datatype):
    rval1 = format(val1*1000000000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval2 = format(val1*1000000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval3 = format(val1*1000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval4 = val1
    rval5 = format(val1/1000, ",").replace(".","%").replace(",",".").replace("%",",")
    print(rval1,"µ",datatype)
    print(rval2,"m",datatype)
    print(rval3,datatype)
    print(rval4,"k",datatype)
    print(rval5,"M",datatype)





def calc_values_from_mega(val1,datatype):
    rval1 = format(val1*1000000000000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval2 = format(val1*1000000000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval3 = format(val1*1000000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval4 = format(val1*1000, ",").replace(".","%").replace(",",".").replace("%",",")
    rval5 = val1
    print(rval1,"µ",datatype)
    print(rval2,"m",datatype)
    print(rval3,datatype)
    print(rval4,"k",datatype)
    print(rval5,"M",datatype)






def option_1():
    print("You selected conversion calculation.")
# Handling Value Error
    try:
        name = input("Enter your unit (µ, m‚ a, k, M): ")
        datatype = input("Enter your unit type (V - Volt, Ω - Ohm,W - Watt, A - Amp): ")
        print("Enter your", name, "value: ")
        val1 = int(input("value: "))
        print("The entered value is:", val1,name,datatype)
        if name == "µ":
            calc_values_from_mikro(val1,datatype)
            pass
        if name == "m":
            calc_values_from_mili(val1,datatype)
            pass
        if name == "a":
            calc_values_from_actual(val1,datatype)
            pass
        if name == "k":
            calc_values_from_kilo(val1,datatype)
            pass
        if name == "M":
            calc_values_from_mega(val1,datatype)
            pass

    except ValueError:
        print("Invalid input. Please enter an integer. Returning to main menu.")
    # Add your command logic here for Option 1

def option_2():
    print("You selected Parallel Total resistance calculation.")
    # Ask user for amount of resistors
    n = int(input("Enter your amount of resistors: "))
    # Below line read inputs from user using map() function
    a = list(map(float,input("\nEnter the numbers : ").strip().split()))[:n]
    #print("\nList is - ", a)
    lst = []
    for val in a:
        #print(val)
        valcal = math.pow(val,-1)
        #print(valcal)
        lst.append(valcal)

        pass
    #print(lst)
    #sum(lst)
    totalR = math.pow(sum(lst),-1)
    print("Total Calculated resistance: ", totalR, "Ω")
    # Add your command logic here for Option 2

def option_3():
    print("You selected Option 3.")
    # Add your command logic here for Option 3

def option_4():
    print("You selected Option 4.")
    # Add your command logic here for Option 4

def main_menu():
    print("Welcome to the Main Menu!")
    print("1. Convert to µ, m, actual, k and M")
    print("2. Parallel resistance - Calculate total resistance")
    print("3. Option 3")
    print("4. Option 4")
    print("0. Exit")




    while True:
        choice = input("Enter your choice (0-4): ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "0":
            print("See you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
