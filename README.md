# Computer Vision: Rock-Paper-Scissors
> Rock-paper-Scissors is a two-player game where players make a shape with their hand that represents either rock, paper or scissors and they win based on what shape they and the opposing player made. For example, a player that chooses rock will win if their oppenent chooses scissors but lose if they chose paper. In the same way, if a player chooses scissors wil win if the oppenent chooses paper but lose if they chose rock.
---
## Teachable-Machine & OpenCV

In this project, Teachable-Machine is used to create the Keras model for the rock-paper-scissors game. This model will recognise the hand gesture that represents either rock, paper or scissors using the camera. The model is trained by taking multiple pictures of the user's hand and making each gesture at different positions on the camera. The more pictures that are taken, the more accurately the camera can recognise each gesture. The model will be downloaded as 'keras_model.h5'. This model will be used in the project in the python code to the recognise each gesture. Here, the OpenCV python library is used to access the camera to play the game.

The code below shows the script that loads the model downloaded from Teachable-Machine and uses the OpenCV library to access the camera.Here, the NumPy library will be used to obtain the prediction for which hand gesture is detected from the camera.  
```python
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    user_output = np.argmax(prediction[0]) # Obtains the predicted hand gesture  
    print(user_output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
```

---
## Manual Rock-Paper-Scissors
This milestone uses the code below that runs a manual game without the camera. Initially two functions were created, where the first one is coded so the computer randomly picks one of the three options using the random module. Then the second function will ask the user to input their option. 
```python
import random
options = ['rock', 'paper', 'scissors']

def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    user_choice = input( 'Choose option: ')
    return user_choice
```
Then a third function called `get_winner` that contains the logic of the game is created  using if and elif statements that takes in options returned from the first two functions to match the  conditions of the game. Finally the final function, `play` is created to call the previous functions to run the game. 
```python
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
---
## Rock-Paper_Scissors using Camera 
Here, is the finished code for the rock-paper-scissors game is created within the `rps` class which takes an input from the camera and captures the gesture from my hand by incorporating the Keras model into the code. The class first initializes the number of wins for the user and player after each round and the three options that are randomly selected by the computer. Then the first method which is `get_prediction` uses the Keras model to return the input from the camera. The input for the user is given by the `np.argmax(prediction[0])`which provides the element that the camera recognises the most. Then the `get_winner` method takes the user input and the computer input from the `get_computer_choice` to see who won the round and then adds the win to either the `self.user_wins` or `self.computer_wins` attributes that were initialised earlier. Finally, outside of the class, the `play` function which would call the methods in the class if the number of wins of each player is less than three and then tells the user who won after a player wins three rounds.
```python
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

options = ['rock', 'paper', 'scissors']

class rps:
    def __init__(self, options, computer_wins = 0, user_wins = 0):
        self.options = options #
        self.computer_wins = computer_wins # number of rounds the computer has won
        self.user_wins = user_wins  # number of rounds the user has won

    def get_prediction(self):

        start = time.time()

        while True: 
            
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            self.user_choice = np.argmax(prediction[0])
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            end = time.time()
            countdown = end - start
            if countdown > 4:
                print(countdown)
                break
            


        return self.user_choice

    def get_computer_choice(self):
        self.computer_choice = random.choice(options)
        return self.computer_choice


    def get_winner(self):

        print('computer played {}'.format(self.computer_choice))


        if self.user_choice == 0 :                             
            print('You played rock')
            if self.computer_choice == 'rock':
                print('It is a tie!')
            elif self.computer_choice == 'scissors':
                print('You win this round!')
                self.user_wins = self.user_wins + 1           
            elif self.computer_choice == 'paper':
                print('You lose this round!')
                self.computer_wins = self.computer_wins + 1

        elif self.user_choice == 1 :
            print('You played paper')
            if self.computer_choice == 'rock':
                print('You win this round!')
                self.user_wins = self.user_wins + 1
            elif self.computer_choice == 'scissors':
                print('You lose this round!')
                self.computer_wins = self.computer_wins + 1
            elif self.computer_choice == 'paper':
                print('It is a tie!')

        elif self.user_choice == 2 :
            print('You played scissors')
            if self.computer_choice == 'paper':
                print('You win this round!')
                self.user_wins = self.user_wins + 1
            elif self.computer_choice == 'rock':
                print('You lose this round!')
                self.computer_wins = self.computer_wins + 1
            elif self.computer_choice == 'scissors':
                print('It is a tie!')

        elif self.user_choice == 3:
            print('Camera did not regconise input. Plesae try again!')

            return self.computer_wins, self.user_wins


def play(options):
    game = rps(options, computer_wins = 0, user_wins = 0)
    while True:
        if game.user_wins < 3 and game.computer_wins < 3:
            game.get_prediction()
            game.get_computer_choice()
            game.get_winner()
            print(game.computer_wins, game.user_wins)
        elif game.user_wins == 3:
            print('Contragulations, you won the game!')
            break
        elif game.computer_wins == 3:
            print('Sorry, you lost the game!')
            break


play(options)
cap.release()
cv2.destroyAllWindows()  
```
