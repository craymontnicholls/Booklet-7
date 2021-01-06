#has a set PiN value that the user has to know to get in 
def checker():
  PIN = ("1234")
  count = 0
  while count < 3: 
    #if the user inputs an innocorrect pin 3 times after that they become locked out
    
    userPIN = input("Enter your PIN")

    if userPIN == PIN:
      print ("Hello")
      break
    else:
      print("Wrong PIN")
      count = count + 1
    if count == 3:
      print("Locked out")


checker()