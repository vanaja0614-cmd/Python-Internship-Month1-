# Temperature Converter

choice = input("Convert Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F): ")

if choice.upper() == "C":
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit:", f)

elif choice.upper() == "F":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius:", c)

else:
    print("Invalid Choice")