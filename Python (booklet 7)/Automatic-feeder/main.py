#tells the user what hopper and how many times it needs to be dispensed
def feeder(meal, amount):
  if meal == "Breakfast":
    print ("Hopper1," * amount)
  elif meal == "Lunch":
    print ("Hopper2," * amount)
  elif meal == "Dinner":
    print ("Hopper1 ,Hopper2 ," * amount) 
    #the '* amount' makes the string repeat a set number of times

feeder("Lunch", 100000000 )