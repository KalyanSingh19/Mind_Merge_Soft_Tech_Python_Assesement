#Scope Resultion in Python
x = 10  # Global scope

def outer_function():
    y = 20  # Enclosing scope

    def inner_function():
        z = 30  # Local scope
        print(x)  # Accesses global variable
        print(y)  # Accesses enclosing variable
        print(z)  # Accesses local variable

    inner_function()

outer_function()
