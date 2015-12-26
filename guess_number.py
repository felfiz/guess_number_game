import random

right_number = random.randint(1, 10)

while True:
  print("Guess the number... ")
  try_number = input("> ")

  if try_number == right_number:
    print("You got it :)")
  else:
    if try_number < right_number:
      print('The number is greater than {}'.format(try_number))
    else:
      print('The number is lesser than {}'.format(try_number))