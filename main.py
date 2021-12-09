import random

print(""" /$$$$$$$  /$$$$$$$   /$$$$$$ 
| $$__  $$| $$__  $$ /$$__  $$
| $$  \ $$| $$  \ $$| $$  \__/
| $$$$$$$/| $$$$$$$/|  $$$$$$ 
| $$__  $$| $$____/  \____  $$
| $$  \ $$| $$       /$$  \ $$
| $$  | $$| $$      |  $$$$$$/
|__/  |__/|__/       \______/ 
                              
                              
                              """)

choices = {'rock': 1, 'paper': 2, 'scissors': 3}
choices1 = ['rock', 'paper', 'scissors']
rock = False
paper = False
scissors = False

while True:
    while True:
        player = input('Welcome! Please choose Rock, Paper or Scissors\n> ').lower()

        if player in choices1:
            break
        else:
            print('Please enter Rock, Paper or Scissors!')

    bot = random.choice(list(choices.values()))

    player = choices.get(player)

    diff = bot-player

    if diff in [-1, 2]:
        print('You lose!')
    elif diff in [-2, 1]:
        print('You win!')
    else:
        print('Its a tie!')

    play_again = input('Do you want to play again? (y/n) > ')
    if play_again == 'y':
        pass
    else:
        print('Game over!')
        break