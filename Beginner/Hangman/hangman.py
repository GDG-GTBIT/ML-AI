import random
import time

print("\nWelcome to Hangman Game!!!\n")
print("You have to guess the name of fruits")
time.sleep(2)
print("The game is about to start\n")
time.sleep(3)

def main():
    global count
    global display
    global fruit
    global already_guessed
    global length
    global play

    fruitList = ["mango","banana","cherry","strawberry","apple","grapes","melon","watermelon","papaya"]
    fruit = random.choice(fruitList)
    length = len(fruit)
    count = 0
    display = '_ '*length
    already_guessed = []
    play = " "

#play loop
def play_loop():
    global play
    play = input("Do you want to play again? (yes/no): ")
    while play not in ["yes","no"]:
        play = input("Do you want to play again? (yes/no): ")
    if play == "yes":
        main()
    elif play == "no":
        print("Thanks for playing!!!")
        exit()

#game
def hangman():
    global count
    global display
    global fruit
    global already_guessed
    global play
    limit = 5
    print("This is the Hangman Word: " + display + "\n")
    guess = input("Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input...Enter a character\n")
        hangman()
    elif guess in fruit:
        already_guessed.extend([guess])
        index = fruit.find(guess)
        fruit = fruit[:index] + "_" + fruit[index+1:] 
        display = display[:index]+guess+display[index+1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter\n")
    else:
        count+=1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,fruit)
            play_loop()

    if fruit == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()

