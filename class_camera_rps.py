import random
import time

import cv2
import numpy as np
from keras.models import load_model

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

options = ['rock', 'paper', 'scissors']

class rps:
    def __init__(self, options, computer_wins = 0, user_wins = 0):
        self.options = options
        self.computer_wins = computer_wins
        self.user_wins = user_wins

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
            # Press q to close the window
            # print(prediction) 
            self.user_choice = np.argmax(prediction[0])
            # print(user_choice) 
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


