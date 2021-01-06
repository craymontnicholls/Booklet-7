def GetInput():
  print("1. Option A")
  print("2. Option B")
  Valid = False
  Choice = ""
  while not Valid:
    Choice = input("Enter an option number: " ).lower()
    if Choice == "a" or Choice == "b" or Choice == "option a" or Choice == "option b":
      Valid = True
    else:
      print("Invalid option chosen. Try again.")
  return Choice

Choice = GetInput()
print("You chose option {}".format(Choice))
    


