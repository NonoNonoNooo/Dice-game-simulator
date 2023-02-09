'''Dice game simulator'''

from random import randint

def random_dice():
    return randint(1, 6)

player = []
bot = []

print('''Hi this is a craps game simulator
the rules of the game are these
- player and computer roll dice simultaneously 
- player and computer scores are counted for 3 rounds 
- winner who has more points after 3 rounds\nLet the games begin\n''')

yes_no = input('Do you want to start\nYes or No -> ')

if yes_no[0] in 'Nn':
    print('Goodbye')

else:
    while True:

        for i in range(3):
            print(f'\nRound {i+1}')
            player.append(random_dice() + random_dice())
            bot.append(random_dice() + random_dice())
            print(f'----------------\nOur results are as follows\nPLayer -> {player[-1]}\nBot -> {bot[-1]}\n****************')

        print(f'\nResults for 3 rounds are as follows\nSack ball player -> {sum(player)}\nSack ball bot -> {sum(bot)}')

        if sum(player) > sum(bot):
            print('Player WIN')
        elif sum(player) < sum(bot):
            print('Bot Win')
        else:
            print('We have a tie')

        y_n = input('Want to play again?\nYes or No')

        if y_n[0] in 'Nn':
            print('Goodbye')
            break
        else:
            player = []
            bot = []