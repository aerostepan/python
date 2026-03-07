from script1 import *

def fav_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script 2")
    fav_food("sushi")
    fav_drink("Coffe")
    print("Goodbye")

if __name__ == '__main__':
    main()