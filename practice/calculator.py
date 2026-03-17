num_a = float(input("Enter the 1st Number: "))
num_b = float(input("Enter the 2nd Number: "))
operation = input("Which operation do you want to perform?(*,+,-,/): ")

if operation == "*":
    suma = num_a * num_b
elif operation == "+":
    suma = num_a + num_b
elif operation == "-":
    suma = num_a - num_b
elif operation == "/":
    if num_a == 0:
        print("Cannot divide by 0!")
    else:
        suma = num_a / num_b
elif operation == "":
    print("You did not input an operation!")
else:
    print(f"Operation {operation} does not exist!")
    

try:
    suma
except NameError:
    print("Try again")
else:
    print(f"Result: {round(suma, 2)}")