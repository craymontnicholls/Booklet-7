#program converts feet to meters and stone to kg
def Utility(unit, amount):
  if unit == "feet":
    amount1 = amount * 0.3048
    print("{} feet is equal to {} meteres".format(amount, amount1))
  elif unit == "stone":
    amount1 = amount * 6.35029
    print("{} stone is equal to {} kg".format(amount, amount1))
  


Utility("stone", 10000)
#the code in the fucntion could be repeated for other metrics  
