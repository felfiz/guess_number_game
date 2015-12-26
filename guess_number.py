import random

right_number = random.randint(1, 10)

while True:
  print("Guess the number... ")
  secret_number = input("> ")

  if secret_number == right_number:
    print("You got it :)")
  else:
    if secret_number < right_number:
      print('The number is greater than {}'.format(secret_number))
    else:
      print('The number is lesser than {}'.format(secret_number))