import random

def GetInput():
  Number = input("Enter a number:")
  if Number.isnumeric():
    ValidInput = True

    ValidInput = False
    while not ValidInput:
      return int(Number)

print(GetInput())

def GuessTheNumber():
  
  random.seed()
  CPU = random.randint(1,100)
  PlayerGuess = 0
  GuessCount = 0
  
  while PlayerGuess != CPU:
    PlayerGuess = GetInput()
    if PlayerGuess < CPU:
      print("Too low")
    elif PlayerGuess > CPU:
      print("Too high")
    
    GuessCount = GuessCount + 1
  
  
  print("You've got it, I chose {}. It took you {} guesses".format(CPU, GuessCount))


GuessTheNumber()