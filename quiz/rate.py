
# hours = float(input("Enter  number of hours: "))
# rate = float(input("Enter  rate per hour: "))

# pay = 0

def computepay(hours, rate):
  if hours > 40:
    pay = (40 * rate) + (hours - 40) *(rate * 1.5)
  else:
    pay = hours * rate
  return pay

print(computepay(45, 10))

# hours = 41
# rate = 2

# pay = (40 * 2) + (1 *(1 * 15))
#  total = 80 + 1.5 = 81.5


