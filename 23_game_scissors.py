from enum import Enum
import random

GREETING = '''
Enter data 
    0 - ROCK
    1 - PAPPER
    2 - SCISSORS
    \'q\' for exit: '''

ROCK, PAPER, SCISSORS = range(3)

def code2text(code):
    if code == ROCK:
        return 'ROCK'
    elif code == PAPPER:
        return 'PAPPER'
    elif code == SCISSORS:
        return 'SCISSORS'


def who_is_winner(pc_choice, user_choice):
    if pc_choice == ROCK and user_choice == SCISSORS:
        return False
    if pc_choice == PAPPER and user_choice == ROCK:
        return False
    if pc_choice == SCISSORS and user_choice == PAPPER:
        return False
    return True


def game():

    while True:
        input_data = input(GREETING)
        if input_data == 'q':
            break

        if not input_data.isnumeric():
            print('Invalid data')
            continue

        if not ROCK <= int(input_data) <= SCISSORS:
            print('Invalid data')
            continue

        pc_choice = random.randint(ROCK, SCISSORS)
        user_choice = int(input_data)

        print('PC choice: %s' % code2text(pc_choice))
        if pc_choice == user_choice:
            print('Tie')
        else:
            if who_is_winner(pc_choice, user_choice):
                print('User is winner: %s vs %s' %
                      (code2text(pc_choice),
                       code2text(user_choice)))
            else:
                print('PC is winner: %s vs %s' %
                      (code2text(pc_choice),
                       code2text(user_choice)))

game()


