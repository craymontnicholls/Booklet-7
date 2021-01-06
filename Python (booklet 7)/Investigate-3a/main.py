import random

def GetInput():
  print("What do you think the dice rool will be?")
  ValidChoice = False
  while not ValidChoice:
    Choice = int(input("Enter a guess between 1 and 6:"))
    
    if 6 <= Choice <= 1:
      ValidChoice = True
    if not ValidChoice:
      print("Invalid choice.")
  return Choice


random.seed()
Roll = random.randint(1,6)
Choice = GetInput()
print("The roll was {}, you guessed {}".format(Roll, Choice))