import cv2
import numpy as np
from keras.models import load_model
import random
import time



model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

options = ['rock', 'paper', 'scissors']


def get_prediction():

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
        user_choice = np.argmax(prediction[0])
        # print(user_choice) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        end = time.time()
        countdown = end - start
        if countdown > 4:
            print(countdown)
            break
       


    return user_choice


def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice

def get_winner(computer_choice, user_choice, computer_wins, user_wins):

    print('computer played {}'.format(computer_choice))


    if user_choice == 0 :
        print('You played rock')
        if computer_choice == 'rock':
            print('It is a tie!')
        elif computer_choice == 'scissors':
            print('You win!')
            user_wins = user_wins + 1           
        elif computer_choice == 'paper':
            print('You lose!')
            computer_wins = computer_wins + 1

    elif user_choice == 1 :
        print('You played paper')
        if computer_choice == 'rock':
            print('You win!')
            user_wins = user_wins + 1
        elif computer_choice == 'scissors':
            print('You lose!')
            computer_wins = computer_wins + 1
        elif computer_choice == 'paper':
            print('It is a tie!')

    elif user_choice == 2 :
        print('You played scissors')
        if computer_choice == 'paper':
            print('You win!')
            user_wins = user_wins + 1
        elif computer_choice == 'rock':
            print('You lose!')
            computer_wins = computer_wins + 1
        elif computer_choice == 'scissors':
            print('It is a tie!')

    elif user_choice == 3:
        print('Camera did not regconise input. Plesae try again!')

    return computer_wins, user_wins
    

def play():
    computer_wins = 0
    user_wins = 0
    while True:
        if user_wins < 3 and computer_wins < 3:
            user_choice = get_prediction()
            computer_choice = get_computer_choice()
            computer_wins, user_wins = get_winner(computer_choice, user_choice, computer_wins, user_wins)
            print(computer_wins, user_wins)
        elif user_wins == 3:
            print('Contragulations, you won the game!')
            break
        elif computer_wins == 3:
            print('Sorry, you lost')
            break


play()
cap.release()
cv2.destroyAllWindows()

