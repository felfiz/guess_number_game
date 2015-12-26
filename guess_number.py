import random

right_number = random.randint(1, 10)

while True:
  print("Guess the number... ")
  try_number = input("> ")

  if try_number == right_number:
    print("You got it :)")
  else:
    print('You Fail! Try again')