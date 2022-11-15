import random
options = ['rock', 'paper', 'scissors']

def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    user_choice = input( 'Choose option: ')
    return user_choice


def get_winner(computer_choice, user_choice):

    print('computer chose {}'.format(computer_choice))

    if user_choice == 'rock':
        if computer_choice == 'rock':
            print('It is a tie!')
        elif computer_choice == 'scissors':
            print('You won!')
        elif computer_choice == 'paper':
            print('You lose!')

    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('You won!')
        elif computer_choice == 'scissors':
            print('You lose!')
        elif computer_choice == 'paper':
            print('It is a tie!')

    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print('You won!')
        elif computer_choice == 'rock':
            print('You lose!')
        elif computer_choice == 'scissors':
            print('It is a tie!')
    
    else:
        print('Invalid option')
    
    
def play():
    get_winner(get_computer_choice(), get_user_choice())

play()
    