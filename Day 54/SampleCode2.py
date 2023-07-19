# Functions in Python are counted as first class objects. This means that they can be passed as arguments to other functions, returned as values from other functions, and assigned to variables and stored in data structures.

def add(a, b):
    return a + b

def operate(func, a, b):
    return func(a, b)

print(operate(add, 1, 2))


# Functions can also be defined inside other functions. Such functions are called nested functions. Nested functions can access variables of the enclosing scope and can only be called in the scope in which they are defined.

def outer_funct():
    message = "Hello"
    def inner_func():
        print(message)
    return inner_func()

outer_funct()

# Functions can be returned as well in Python. This is a very powerful feature of Python. This is called a closure. A closure is an inner function that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing.

def outer_func():

    message = "Hello"

    def inner_func():
        print(message)

    return inner_func

inner_func = outer_func()
inner_func()