class Decorator:
    def __init__(self, passed_function):
        self.func = passed_function


    def __call__(self, *args, **kwargs):
        print("This line is within the decorator, it and the next 4 lines are executed before the called function:")
        print("\tA decorator has been called on:", self.func.__name__)
        print("\tThe called function's arguments are:")
        print("\t\t{}".format(args))
        print("\t\t{}".format(kwargs))
        print()
        self.func(*args, **kwargs)
        print("This line is within the decorator class but is executed after the called function. It is the fifth and final line.")

@Decorator
def new_function(*args, **kwargs):
    print("This line is within the function, it and the next 3 lines constitute the entirety of the called function:")
    print("\tI am new_function and I was called.")
    print("\t\t{}".format(args))
    print("\t\t{}".format(kwargs))
    print()

print("A function will be called with a single decorator.\n")
new_function("I'm the first positional argument.", "I'm the second positional argument.", exec="I am the only keyword argument.")