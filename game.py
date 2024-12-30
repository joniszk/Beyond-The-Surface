import random
import functions

questions = []
game_continue = True

#introduce user to game
functions.introduction()

while game_continue:
    #get level from the user
    level = functions.get_level()

    #load questions into an arraylist
    questions = functions.load_questions(level)

    #randomize the question order
    random.shuffle(questions)

    #display questions to user one by one
    functions.display_questions(questions)

    #Ask user if they want to play again
    game_continue = functions.replay()
else:
    print("Thank you for playing!")