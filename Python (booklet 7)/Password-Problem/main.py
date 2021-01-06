import re
#checks to see if the password has the reqired things
def validation():
  while True:
    password = input("Enter your password")
    if len(password) < 8:
      print("the password needs to be at least 8 letters long")
    elif re.search ('[0-9]', password) is None:
      print("make sure u have a number in the password")
    elif re.search ('[A-Z]', password) is None:
      print("make sure u have a capital letter in your password")
    else:
      print("your password is good")
      break


validation()


