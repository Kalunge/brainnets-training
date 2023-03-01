def computegrade(score):
    try:
      if score > 1.0 or score < 0.0:
        print("score is out of range")
      elif score >= 0.9:
        print("A")
      elif score >= 0.8:
        print("B")
      elif score >= 0.7:
        print("C")
      elif score >= 0.6:
        print("D")
      else:
        print("E")
    except ValueError:
      print("Enter a valid integer or float")

computegrade(0.95)
computegrade(0.85)
computegrade(0.75)
computegrade(0.65)
computegrade(0.55)

# try:
#   score = float(input("Enter score between 0.0 and 1.0: "))
#   if score > 1.0 or score < 0.0:
#     print("score is out of range")
#   elif score >= 0.9:
#     print("A")
#   elif score >= 0.8:
#     print("B")
#   elif score >= 0.7:
#     print("C")
#   elif score >= 0.6:
#     print("D")
#   else:
#     print("E")
# except ValueError:
#   print("Enter a valid integer or float")



