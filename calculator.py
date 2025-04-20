import math

print("welcome to the world of math!!")

print("choose any operation:")

print("1.sine")
print("2.cosine")
print("3.tan")
print("4.exponent")
print("5.logarithm(base 10)")
print("6.square Root")
print("7.Factorial")
print("8.addition")
print("9.subtraction")
print("10.multiplication")
print("11.division")
print("12.remainder")
print("13.round-off")

user_choice =int(input("Enter your operation need to be performed(1 to 13):"))


if user_choice == 1:
    x = int(input("Enter the angle in degrees:"))
    radians = math.radians(x)
    result = math.sin(radians)
    print(f" sine value  is {result}")
    
elif user_choice == 2:
    x = int(input("Enter the angle in degrees :"))
    radians = math.radians(x)
    result =math.cos(radians)
    print(f"cosine value is {result}")
    
elif user_choice == 3:
    x = int(input("Enter the angle in degrees :"))
    radians = math.radians(x)
    result =math.tan(radians)
    print(f" the tan value is {result}")
    
elif user_choice == 4:
    x = int(input("Enter base number (x): "))
    y = int(input("Enter exponent (y): "))
    result = math.pow(x,y)
    print(f"{x} raised to the power {y} is {result}")

elif user_choice == 5:
    x = int(input("Enter a number: "))
    result = math.log10(x)
    print(f"Log base 10 of {x} is {result}")

elif user_choice == 6:
    x = int(input("Enter a number: "))
    result = math.sqrt(x)
    print(f"Square root of {x} is {result}")

elif user_choice == 7:
    x = int(input("Enter an integer: "))
    result = math.factorial(x)
    print(f" Factorial of {x} is {result}")

elif user_choice == 8:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")

elif user_choice == 9:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")

elif user_choice == 10:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")

elif user_choice == 11:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Division by zero is not allowed.")

elif user_choice == 12:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 % num2
    print(f"The remainder when {num1} is divided by {num2} is {result}")

elif user_choice == 13:
    num = float(input("Enter a number: "))
    result = round(num)
    print(f"The rounded value of {num} is {result}")

else:
    print("Invalid choice.")