def is_palindrome():
  str = input("Enter a string to check if it is a plaindrome: ")
  # claen the string to remove any spaces using replae and then convert to lower case
  cleaned_str = str.replace(" ", "").lower()
  # reverse the string then remove all
  reversed_str =  cleaned_str[::-1]

  # compare both strings

  print(cleaned_str == reversed_str)


  # combined operations 
  #  return str.replace(" ", "").lower() == str[::-1].replace(" ", "").lower()




is_palindrome()

