import random
number = random.choice(range(1,101))
attempt = 0
guess = -1
win = False
def check(num,guess):
    if num > guess:
        print("Too low")
    elif num < guess:
        print("Too high")
    else:
        print(f"You guessed the correct number! The number is {num}! You Win! ")
        win = True

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempt = 10
else:
    attempt = 5

while guess != number and attempt > 0:
    if attempt >0:
        print(f"You have {attempt} attempts left")
    elif attempt == 1:
        print(f"You have {attempt} attempt left")
    attempt -=1

    guess = int(input("Make a guess: "))

    check(number, guess)


if not win:
    print(f"You ran out of tries !You lost haha! The number was {number}")



