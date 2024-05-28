# Decorators
def timed_greet(fn):
    def wrapper(*args, **kwargs):
        print('Good Morning!')
        fn(*args, **kwargs)
    return wrapper

def greet_2():
    print('Allan')

greet_2 = timed_greet(greet_2)#Decorator

greet_2()

@timed_greet()
def greet(name):
    print(name)

greet = timed_greet(greet)

greet('Gerald')

def format_square(fn):
    def wrapper (*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'The square of {args[0]} is (result)')
    return wrapper


def square (number):
    return number*number

square(10)
print (square(7))