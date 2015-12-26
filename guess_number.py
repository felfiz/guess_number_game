import random

def guess_game():
  right_number = random.randint(1, 10)
  guesses = []

  while len(guesses) < 3:
    print("Guess a number between 1 and 10")
    try:
      secret_number = int(input("> "))
    except ValueError:
      print('{} is not a number'.format(secret_number))
    else:
      guesses.append(secret_number)

      if secret_number == right_number:
        print("You got it :)")
        break
      else:
        if secret_number < right_number:
          print('The number is greater than {}'.format(secret_number))
        else:
          print('The number is lesser than {}'.format(secret_number))
  else:
    print("Sorry you lose :( . My number was {}".format(right_number))
guess_game()