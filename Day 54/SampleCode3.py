import time

# The below function takes a function as an argument and puts a delay of 2 seconds before executing it
def delay_decorator(function):
    def wrapper():
        time.sleep(2)
        #Do something before
        function()
        #Do something after
    return wrapper

# We use a decorator for the functionality of the delay_decorator function. It uses the function just below it as an argument.
@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

