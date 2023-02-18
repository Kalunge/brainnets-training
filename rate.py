hours = float(input("Enter  number of hours: "))
rate = float(input("Enter  rate per hour: "))

pay = 0



if hours > 40:
  try:
    pay = (40 * rate) + (hours - 40) *(rate * 1.5)
  except:
    print("An exception occurred")
else:
  pay = hours * rate




print(f"your pay is {pay}")

# hours = 41
# rate = 2

# pay = (40 * 2) + (1 *(1 * 15))
#  total = 80 + 1.5 = 81.5


