score = 120
if score > 100:
  print("You have got over 100 points!")
print('\n')

score = 80
if score > 100:
  print("You have got over 100 points!")
else:
  print("Keep going!")
print('\n')

score = 110
timePlayed = 80
if score > 100 and timePlayed > 60:
  print("You have completed the level!")
else:
  print("Keep going!")
print('\n')

username = "Rob"
if username == "Rob":
  print("Hi Rob!")
else:
  print("I don't know you.")
print('\n')

username = "Dave"
if username == "Rob":
  print("Hi Rob!")
elif username == "Kirsten":
  print("Hi Kirsten!")
else:
  print("I don't know you.")
print('\n')

username = "rob"
password = "myPassword"
if username == "rob" and password == "myPassword":
  print("Correct, you are logged in!")
elif username == "rob" and password != "myPassword":
  print("Your password is wrong.")
elif username != "rob" and password == "myPassword":
  print("Your username is wrong.")
else:
  print("Both your username and password are wrong.")
print('\n')

