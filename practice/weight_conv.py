weight = input("Enter your weight: ")
dig_weight = weight.isdigit()
if dig_weight:
    weight = float(weight)

unit = input("Enter weight unit(kg/lbs): ")

if dig_weight == False:
    print("Weight must be a digit!")
elif weight == 0:
    print("You weigh nothing!")
elif unit == "kg":
    weight = weight * 2.205
    print(f"Your weight in pounds is: {round(weight,2)}lbs")
elif unit == "lbs":
    weight = weight / 2.205
    print(f"Your weight in kilograms is: {round(weight,2)}kg")
elif unit == "":
    print("No unit selected! Try again")
else:
    print(f"{unit} is not a correct unit!")


