# 5. Write a program that prompts the user for a number and checks whether the number is a prime number
# (i.e., only divisible by 1 and itself).


def is_prime(number):
    factors = []

  # iterate over all numbers from 1 to given number and check if they are divisible, add them to factors list if they are divisible
    for num in range(1, number):
        if number % num == 0:
            factors.append(num)

  # a prime number should have only two factors therefore return false if otherwise
    if len(factors) > 2:
      print("False")
    else:
      print("True")


is_prime(3)
is_prime(2)
is_prime(98)
is_prime(29)
is_prime(37)
