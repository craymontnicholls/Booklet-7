def GetInput():
  print("1. Option 1")
  print("2. Option 2")
  print("3. Option 3")
  Choice = input("Enter an option number: ")
  return int(Choice)

Choice = GetInput()
if Choice > 3:
  print("Error")
elif Choice == str:
  print("Error")
else:
  print("You chose option {}".format(Choice))