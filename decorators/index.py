# write a function named greet(func)

# inside greet(func) create another function that does the following:
# 	1. print something
# 	2. a variable that uses func to access different arguments (*args)

# define another function called say_hello() which prints something
# and by calling say_hello() at the end, also the greet(func) should be
# provoked.

def greet(func):
    def wrapper(*args):
        print("Hello")
        func(*args)
    return wrapper

@greet
def say_hello(name):
    print(f"My name is {name}")

say_hello("John")



 

#  2.
# write a function called authorize(func)
# define a wrapper (func inside another func) inside and return
# "Unathorized access" if not authorized.
# define another function to check whether authorized or not. (True or False)
# define the last function named secret_data() 
# to say "This is confidential data" if user is authorized.
# By calling secret_data you should see if the data is confidential or 
# you will provoke the other function that says "Unauthorized access".

def authorize(func):
    def wrapper(*args):
        if not is_authorized:
            return "Unauthorized access"
        return func(*args)
    return wrapper

def check_auth():
    return True

@authorize
def secret_data():
    print("This is confidential data")

is_authorized = check_auth()
secret_data()




# 3.
# write a function called validate(func), define a wrapper inside,
# see if arguments were not integer, return and error.
# define a function called add(a, b).
# when calling the func add() in the end, if the args are integers return 
# the sum, if even one of them in str, return that error you defined in the
# first function.

def validate(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) != int:
                return "Invalid input"
        return func(*args)
    return wrapper

@validate
def add(a, b):
    return a + b


print(add(1, 2))
print(add(1, "2"))

