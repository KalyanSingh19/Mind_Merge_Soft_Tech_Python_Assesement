def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Wh0's There??")
        result = func(*args, **kwargs)
        print("Come Inside")
        return result
    return wrapper

@my_decorator
def greet(name):
    print("Hello, " + name + "!")

greet("Kalyan")