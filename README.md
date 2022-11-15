# Computer Vision: Rock-Paper-Scissors
> Rock-paper-Scissors is a two- player game where players make a shape with their hand that represents either rock, paper or scissors and they win based on what shape they and the opposing player made. For example, a player that chooses rock will win if their oppenent chooses scissors but lose if they chose paper. In the same way, if a player chooses scissors wil win if the oppenent chooses paper but lose if they chose rock.
---
## Teachable-Machine

In this milestone, I used the Teachable-Machine website to create the model that recognises the hand gesture that represents either rock, paper or scissors using the camera. the model is trained by taking multiple pictures of my hand and making each gesture at different positions on the camera. The more pictures that are taken, the more accurately the camera can recognise each gesture. This model will be used in the project, for the python code, the recognise each gesture when playing the game.

---
## Manual Rock-Paper-Scissors
In this milestone, I created a script that runs the game without the camera. I initially created two functions that where the first one is where the computer randomly picks one of the three options using the random module. Then the second function will ask the user to input their option. Then I created a third function which contains the logic of the game using if and elif statements that takes in options returned from the first two functions to match the  conditions of the game. Finally, a final function was created to call the previous functions. 
```python
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
```
