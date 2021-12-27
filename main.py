import random

num = random.randint(1, 20)
guess = None
user_attempts = 3

while guess != num and user_attempts != 0:
    guess = input("Guess a number between 1 and 20: (You have %s attempts left!) : " % user_attempts)
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break 
    else:
        print("nope, sorry. try again!")
        user_attempts -= 1 
        if user_attempts == 0:
          print("Out of attempts. Game Over!")
          break

