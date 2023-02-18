# 3. Write a program that prompts the user for their age and checks whether they are old enough to vote (i.e., 18 years old or older).

def eligible_to_vote():
  # prompt user to enter their age and convert it into a float
  age = float(input("Enter your current age: "))

  # check if users age is greater than or equal to 18, if meets condition then respond accordingly
  if age >= 18:
    print("You are eligible to vote")
  else:
    print("Sorry! You are not eligible to vote")


eligible_to_vote()