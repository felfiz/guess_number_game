import random

def guess_game():
  secret_number = random.randint(1, 10)
  guesses = []

  while len(guesses) < 3:
    print("Guess a number between 1 and 10")
    try:
      guess_number = int(input("> "))
    except ValueError:
      print('{} is not a number'.format(guess_number))
    else:
      guesses.append(guess_number)

      if guess_number == secret_number:
        print("You got it :)")
        break
      else:
        if guess_number < secret_number:
          print('The number is higher than {}'.format(guess_number))
        else:
          print('The number is lower than {}'.format(guess_number))
  else:
    print("Sorry you lose :( . My number was {}".format(secret_number))
guess_game()