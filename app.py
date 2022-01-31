import random

print('Hello Welcome high/low game')

user_name = input('What is your name ? \n')
guess = random.randint(1, 61)

score = 0

while True:
    print(f"{user_name} guess number is {guess}")
    user_choice = input('h/high or l/low ?')
    user_guess = random.randint(1, 61)
    if user_choice == 'h' and user_guess > guess:
        guess = user_guess
        score += 1
    elif user_choice == 'l' and user_guess < guess:
        guess = user_guess
        score += 1
    else:
        break

print(f'You lose your score is : {score}')