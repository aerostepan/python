weight = float(input("Enter your weight: "))

unit = input("Enter weight unit(kg/lbs): ")

if weight == 0:
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


