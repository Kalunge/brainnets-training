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
        print(
            f"Hello From {self.name}!, I am {self.age} years old and I live in {self.address}, how About you?"
        )


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
        print(
            f"Hello, my name is {self.name} and I am {self.age} years old. I am a student at {self.university}."
        )


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

# Encapsulation: Define a class called Car with private attributes like make, model, and year. Define a method called get_info() that returns a string containing the car's make, model, and year.


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


print(
    starts_with_vowel(
        ["eric", "Titus", "philip", "Matthew", "Esther", "arlette", "John"]
    )
)

# 5. Given a list of dictionaries, write a list comprehension that returns a list of all the values for a given key.


def values_for_key(list_of_dicts, key):
    return [d[key] for d in list_of_dicts]


print(
    values_for_key(
        [{"name": "Monica", "age": 11}, {"name": "James", "age": 40}], "name"
    )
)

# Create a class called Rectangle that has attributes width and height. Add methods area and perimeter that calculate the area and perimeter of the rectangle, respectively.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

        # 3. Create a class called Car that has attributes make, model, and year. Add methods start and stop that simulate starting and stopping the car, respectively.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

        # 2. Create a class called Circle that has attribute radius. Add methods area and circumference that calculate the area and circumference of the circle, respectively.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def circumference(self):
        return 2 * 3.14 * self.radius

        # 1. Create a class called Dog that has attributes name and age. Add methods speak and description that print a sentence with the dog's name and age, respectively.


# 4. Create a class called Dice that has attribute sides (the number of sides on the dice). Add a method roll that generates a random number between 1 and the number of sides on the dice.


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        import random

        return random.randint(1, self.sides)


# 5. Create a class called Temperature that has attribute celsius (a temperature in degrees Celsius). Add methods to_fahrenheit and to_kelvin that convert the temperature to degrees Fahrenheit and Kelvin, respectively.


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15


# 6. Create a class called Book that has attributes title, author, and publication_year. Add a method get_age that calculates how many years ago the book was published.


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        return 2020 - self.publication_year

# 7. Create a class called Rectangle that has attributes width and height. Add methods __str__ and __repr__ that return a string representation of the rectangle object.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


1. 

# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# It is possible to make £2 in the following way:

#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?

def coin_sums():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * 201
    ways[0] = 1

    for coin in coins:
        for i in range(coin, 201):
            ways[i] += ways[i - coin]

    return ways[200]
print(coin_sums())

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
# use class 

class Pandigital:
    def __init__(self):
        self.products = set()

    def is_pandigital(self, n):
        digits = set()
        while n > 0:
            digits.add(n % 10)
            n //= 10
        return len(digits) == 9 and 0 not in digits

    def check(self, a, b):
        c = a * b
        if self.is_pandigital(a) and self.is_pandigital(b) and self.is_pandigital(c):
            self.products.add(c)

    def solve(self):
        for i in range(1, 10000):
            for j in range(i, 10000):
                self.check(i, j)
        return sum(self.products)

print(Pandigital().solve())

# 3. 

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __le__(self, other):
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __ne__(self, other):
        return self.numerator * other.denominator != self.denominator * other.numerator

    def simplify(self):
        for i in range(2, self.numerator + 1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator //= i
                self.denominator //= i
                self.simplify()
                break

    def is_curious(self):
        if self.numerator % 10 == 0 and self.denominator % 10 == 0:
            return False
        if self.numerator % 10 == self.denominator // 10:
            return Fraction(self.numerator // 10, self.denominator % 10) == self
        if self.numerator // 10 == self.denominator % 10:
            return Fraction(self.numerator % 10, self.denominator // 10) == self
        return False

print(Fraction(49, 98).is_curious())