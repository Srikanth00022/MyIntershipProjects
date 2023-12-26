#!/usr/bin/env python
# coding: utf-8

# In[2]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def main():
    print("Welcome to the Unit Converter!")

    try:
        print("Select the conversion type:")
        print("1. Temperature Converter")
        print("2. Length Converter")
        print("3. Weight Converter")

        choice = input("Enter the number corresponding to your choice (1, 2, or 3): ")

        if choice == '1':
            print("\nTemperature Converter")
            temp_choice = input("Select the conversion type:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter the number corresponding to your choice (1 or 2): ")

            if temp_choice == '1':
                celsius = float(input("Enter temperature in Celsius: "))
                result = celsius_to_fahrenheit(celsius)
                print(f"{celsius} Celsius is equal to {result:.2f} Fahrenheit.")
            elif temp_choice == '2':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                result = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit} Fahrenheit is equal to {result:.2f} Celsius.")
            else:
                print("Invalid choice. Please enter 1 or 2.")
        elif choice == '2':
            print("\nLength Converter")
            length_choice = input("Select the conversion type:\n1. Meters to Feet\n2. Feet to Meters\nEnter the number corresponding to your choice (1 or 2): ")

            if length_choice == '1':
                meters = float(input("Enter length in meters: "))
                result = meters_to_feet(meters)
                print(f"{meters} meters is equal to {result:.2f} feet.")
            elif length_choice == '2':
                feet = float(input("Enter length in feet: "))
                result = feet_to_meters(feet)
                print(f"{feet} feet is equal to {result:.2f} meters.")
            else:
                print("Invalid choice. Please enter 1 or 2.")
        elif choice == '3':
            print("\nWeight Converter")
            weight_choice = input("Select the conversion type:\n1. Kilograms to Pounds\n2. Pounds to Kilograms\nEnter the number corresponding to your choice (1 or 2): ")

            if weight_choice == '1':
                kilograms = float(input("Enter weight in kilograms: "))
                result = kilograms_to_pounds(kilograms)
                print(f"{kilograms} kilograms is equal to {result:.2f} pounds.")
            elif weight_choice == '2':
                pounds = float(input("Enter weight in pounds: "))
                result = pounds_to_kilograms(pounds)
                print(f"{pounds} pounds is equal to {result:.2f} kilograms.")
            else:
                print("Invalid choice. Please enter 1 or 2.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()


# In[ ]:




