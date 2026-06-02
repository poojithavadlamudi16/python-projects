def temperature_converter():
    print("\n Temperature Converter")
    print("1.Celsius to Farenheit")
    print("2.farenheit to Celsius")
    print("3.celcius to Kelvin")
    print("4.Kelvin to Celsius")

    choice=input("Enter your choice: ")
    temp=float(input("Enter temerature: "))

    if choice=="1":
        print("Result: ",round((temp*9/5)+32,2),"F")
    elif choice=="2":
        print("Result: ",round((temp-32)*5/9,2),"C")
    elif choice=="3":
        print("Result: ",round(temp+273.15,2),"K")
    elif choice=="4":
        print("Result: ",round(temp-273.15,2),"C")
    else:
        print("Invalid choice.Please select a valid option.")

def length_converter():
        print("\n length Converter")
        print("1.Meter to Kilometer")
        print("2.Kilometer to Meter")
        print("3.Meter to Centimeter")
        print("4.Centimeter to Meter")

        choice=input("Enter your choice: ")        
        value=float(input("Enter length: "))
        if choice=="1":
            print("Result: ",round(value/1000,2),"km")
        elif choice=="2":
            print("Result: ",round(value *1000, 2),"m")
        elif choice=="3":
            print("Result: ",round(value *100, 2),"cm")
        elif choice=="4":
            print("Result: ",round(value /100, 2),"m")
        else:
            print("Invalid choice.Please select a valid option.")
def weight_convereter():
    print("\n weight Converter")
    print("1.Kilogram to Pound")
    print("2.Pound to Kilogram")
    print("3.Kilogram to Gram")
    print("4.Gram to Kilogram")

    choice=input("Enter your choice: ")
    value=float(input("Enter weight: "))
    if choice=="1":
        print("Result: ",round(value*2.20462,2),"lb")
    elif choice=="2":
        print("Result: ",round(value/2.20462, 2),"kg")
    elif choice=="3":
        print("Result: ",round(value*1000, 2),"g")
    elif choice=="4":
        print("Result: ",round(value/1000, 2),"kg")
    else:
        print("Invalid choice.Please select a valid option.")
while True:
    print("\n Unit Converter")
    print("1.Temperature Converter")
    print("2.Length Converter")
    print("3.Weight Converter")
    print("4.Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        temperature_converter()
    elif choice=="2":
        length_converter()
    elif choice=="3":
        weight_convereter()
    elif choice=="4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice.Please select a valid option.")
        