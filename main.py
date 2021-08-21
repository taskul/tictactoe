from random import randint
from collections import OrderedDict

grid_dict = OrderedDict()
def new_board():
    for i in range(1,10):
        grid_dict[i] = " "

def display_grid():
    print(f'''
{grid_dict[1]}|{grid_dict[2]}|{grid_dict[3]}
------
{grid_dict[4]}|{grid_dict[5]}|{grid_dict[6]}
------
{grid_dict[7]}|{grid_dict[8]}|{grid_dict[9]}
''')


def get_oponent_input(oponent, num):
    if oponent == 'X':
        if grid_dict[num] == ' ':
            grid_dict[num] = 'X'
            return True
        else:
            return False
    else:
        if grid_dict[num] == ' ':
            grid_dict[num] = 'O'
            return True
        else:
            return False

def score(oponent):
    if grid_dict[1] == oponent and grid_dict[2] == oponent and grid_dict[3] == oponent:
        return True
    if grid_dict[1] == oponent and grid_dict[5] == oponent and grid_dict[9] == oponent:
        return True
    if grid_dict[1] == oponent and grid_dict[4] == oponent and grid_dict[7] == oponent:
        return True
    if grid_dict[2] == oponent and grid_dict[5] == oponent and grid_dict[8] == oponent:
        return True
    if grid_dict[3] == oponent and grid_dict[6] == oponent and grid_dict[9] == oponent:
        return True
    if grid_dict[4] == oponent and grid_dict[5] == oponent and grid_dict[6] == oponent:
        return True
    if grid_dict[7] == oponent and grid_dict[8] == oponent and grid_dict[9] == oponent:
        return True
    if grid_dict[3] == oponent and grid_dict[5] == oponent and grid_dict[7] == oponent:
        return True

def new_round():
        global game_on
        continue_game = input('Continue? ')
        if continue_game == 'n':
            print('Good bye')
            game_on = False
        else:
            new_board()

def keep_playing(oponent, oponent_score):
    if oponent_score == True:
        if oponent == 'X':
            print('--------GAME OVER---------. Player wins')
            display_grid()
            print('To continue type y for Yes and n for No')
        else:
            print('--------GAME OVER---------. Computer wins')
            display_grid()
            print('To continue type y for Yes and n for No')
        new_round()

game_on = True
new_board()
while game_on == True:
    print('Time to Play Tic Tac Toe')
    print('Directions: type a number to place an X ')
    print('''1: top left, 2: top middle, 3: top right
            4: middle left, 5: middle middle, 6: middle right,
            7: bottom left, 8: bottom middle, 9: bottom right
            0: to exit the game''')

    display_grid()

    player = 'X'
    computer = 'O'
    computer_input = randint(1,9)

    player_input = input('Enter a number: ')
    if player_input == 0:
        print('Good bye')
        game_on = False
    elif bool(player_input) == False:
        print('Please enter a number')
    else:
        player_outcome = get_oponent_input(player, int(player_input))
        while player_outcome == False:
            print('That slot is already taken, please pick another option.')
            player_input = input('Enter a number: ')
            player_outcome = get_oponent_input(player, int(player_input))
        else:
            computer_outcome = get_oponent_input(computer, computer_input)
            while computer_outcome == False:
                board_space = []
                for v in grid_dict.values():
                    board_space.append(v)
                if ' ' not in board_space:
                    print('It is a DRAW')
                    print('Play again? Type y for Yes and n for No')
                    new_round()
                    computer_outcome = True
                else:
                    computer_input = randint(1,9)
                    computer_outcome = get_oponent_input(computer, computer_input)
        player_score = score(player)
        computer_score = score(computer)
        keep_playing(player, player_score)
        keep_playing(computer, computer_score)
            
