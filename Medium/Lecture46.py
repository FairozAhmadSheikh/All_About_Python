# Decorator is a function that extends the behaviour of another function without modifying the base function.
# Pass the base function as an argument to decorator


# Decorator Function
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Here are your sprinkles also ❄️❄️")
        return func(*args, **kwargs)
    return wrapper

# Another Decorator
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Added Fudge also 🍫")
        return func(*args, **kwargs)
    return wrapper

# Base Function
@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    return f"Here is your {flavour} ice cream 🍨"

# Call the function
print(get_ice_cream("chocolate"))
 