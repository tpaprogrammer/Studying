class AdditionDecorator:
    def __init__(self, function):
        self.func = function


    def __call__(self, first_key, second_key):
        if type(first_key) == int and type(second_key) == int:
            self.func(first_key, second_key)
            print(first_key + second_key)
        elif type(first_key) == str and type(second_key) == str:
            self.func(first_key, second_key)
            print(first_key + second_key)
        else:
            print("The decorator only accepts two integers or two strings.")


# Both of the following functions behave the same, meaning either will add two integers or two strings.
# This is just a control flow example for decorator behavior and the concept of edition was used.

@AdditionDecorator
def number_addition(first_key, second_key):
    print("number_addition's first_key type is:", type(first_key))
    print("number_addition's second_key type is:", type(second_key))

@AdditionDecorator
def string_addition(first_key, second_key):
    print("string_addition's first_key type is:", type(first_key))
    print("string_addition's second_key type is:", type(second_key))

number_addition(first_key=1, second_key=2)
string_addition(first_key='a', second_key='b')
number_addition(first_key=1, second_key='b')
string_addition(first_key=1, second_key='b')