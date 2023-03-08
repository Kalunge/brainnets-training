# 1. Create a basic class: Define a class called Person with attributes like name, age, and address. Initialize the class with an instance and print the attributes.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Person: {self.name}, {self.age}, {self.address}"

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def greet(self):
        print(f"Hello From {self.name}!, I am {self.age} years old and I live in {self.address}, how About you?")

person = Person("Matias", 32, "Nairobi")
print(person.name)
print(person.age)
print(person.address)
person.introduce()
person.greet()


# Inheritance: Create a subclass called Student that inherits from the Person class. Add a new attribute called university to the Student class and initialize it in the constructor. Also, override the introduce() method to include information about the student's university.

class Student(Person):
    def __init__(self, name, age, address, university):
        super().__init__(name, age, address)
        self.university = university

    def __str__(self):
        return f"Student: {self.name}, {self.age}, {self.address}, {self.university}"

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a student at {self.university}.")


#  Polymorphism: Define a class Pet with an attribute called name and a method speak(). Create two subclasses Dog and Cat that inherit from the Pet class. Override the speak() method in the Dog and Cat classes to return a string that is specific to each type of pet.

class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am a Pet")

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} says meow!")

dog = Dog("Rex")
dog.speak()

cat = Cat("Fluffy")
cat.speak()

#Encapsulation: Define a class called Car with private attributes like make, model, and year. Define a method called get_info() that returns a string containing the car's make, model, and year. 

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_info(self):
        return f"{self.__make} {self.__model} {self.__year}"

car = Car("Toyota", "Corolla", 2019)
print(car.get_info())

# Class Variables: Define a class BankAccount with a class variable bank_name
#  and instance variables account_holder_name, balance. Initialize the class 
# variables in the constructor and add methods like deposit() and withdraw() 
# to perform transactions. Create two instances of the BankAccount class and 
# verify that the class variable is shared among all instances.

class BankAccount:
    bank_name = "Cooperative Bank of Kenya"

    def __init__(self, account_holder_name, balance):
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"{self.account_holder_name} has {self.balance} in their account."


account1 = BankAccount("Matias", 1000)
account2 = BankAccount("John", 2000)

account1.deposit(100)
account1.withdraw(700)
account2.deposit(700)
account2.withdraw(100)



print(account1)
print(account2)

# 1. Given two lists a and b, write a list comprehension that returns a list of all pairs (x, y) where x is from list a and y is from list b, but only if x is not equal to y.

def pair(a, b):
    return [(x, y) for x in a for y in b if x != y]

print(pair([1, 2, 3], [4, 5, 6]))

# 3. Given a string, write a list comprehension that returns a list of all the vowels in the string.

def vowels(string):
    return [char for char in string if char in "aeiou"]

print(vowels("Matias"))

# 4. Given a list of strings, write a list comprehension that returns a list of all the words that start with a vowel.

def starts_with_vowel(words):
    return [word for word in words if word[0].lower() in "aeiou"] 

print(starts_with_vowel(["eric", "Titus", "philip", "Matthew", "Esther", "arlette", "John"]))

# 5. Given a list of dictionaries, write a list comprehension that returns a list of all the values for a given key.

def values_for_key(list_of_dicts, key):
    return [d[key] for d in list_of_dicts]

print(values_for_key([{"name": "Monica", "age": 11}, {"name": "James", "age": 40}], "name"))