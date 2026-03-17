def add_sprinkles(func):
    def wrapper(*args, **kwargs):#without the internal func, decorator will be called without main func call
        print("*You added sprinkles 🎉*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You added fudge 🍪*")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream 🍨")

get_ice_cream("vanilla")