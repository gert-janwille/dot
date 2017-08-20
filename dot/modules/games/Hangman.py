import time
import random
import dot.common.ui as ui
from dot.common.constants import *

class Hangman():

    def __init__(self):
        print "Starting game..."
        time.sleep(1)
        self.core_game()

    def generateProcess(self, word):
        chars = len(word)
        temp = []

        for char in range(0, chars):
            temp.append('*')
        return temp

    def clearScreen(self):
        window = ui.UiTemplate()
        window.clearScreen()

    def core_game(self):
        guesses = 0
        letters_used = ""
        the_word = random.choice(WORDS).lower()
        progress = self.generateProcess(the_word)

        while guesses < 9:

            guess = raw_input("Guess a letter ->")
            if guess != 'quit':
                if len(guess) > 1:
                    guess = guess[0][:1]
            else:
                break

            self.clearScreen()


            if (guess in the_word) and (guess not in letters_used):
                print '[' + T + '*' + W + '] type `quit` to exit the game'
                print G + "Your guess was RIGHT!" + W
                letters_used +=  guess +","
                self.hangman_graphic(guesses)
                print T + "Progress: " + self.progress_updater(guess, the_word, progress)
                print W + "Letter used: " + letters_used + '\n'

            elif (guess not in the_word) and (guess not in letters_used):
                guesses += 1
                print '[' + T + '*' + W + '] type `quit` to exit the game'
                print R + "Wrong Guess!" + W
                letters_used += guess + ","
                self.hangman_graphic(guesses)
                print T + "Progress: " + "".join(progress)
                print W +"Letter used: " + letters_used + '\n'

            else:
                print '[' + T + '*' + W + '] type `quit` to exit the game'
                print T + "You already typed this letter" + W
                self.hangman_graphic(guesses)
                print T + "Progress: " + "".join(progress)
                print R + "Try again!" + W +'\n'

            if ''.join(progress) == the_word:
                print '[' + T + '*' + W + '] type `quit` to exit the game'
                print T + "You Guessed the word:" + the_word + '\n'
                print  G
                print(" `YMM'   `MM' .g8""8q. `7MMF'   `7MF'     `7MMF'     A     `7MF' .g8""8q. `7MN.   `7MF'")
                print("  VMA   ,V .dP'    `YM. MM       M        `MA     ,MA     ,V .dP'    `YM. MMN.    M  ")
                print("   VMA ,V  dM'      `MM MM       M         VM:   ,VVM:   ,V  dM'      `MM M YMb   M  ")
                print("    VMMP   MM        MM MM       M          MM.  M' MM.  M'  MM        MM M  `MN. M  ")
                print("     MM    MM.      ,MP MM       M          `MM A'  `MM A'   MM.      ,MP M   `MM.M  ")
                print("     MM    `Mb.    ,dP' YM.     ,M           :MM;    :MM;    `Mb.    ,dP' M     YMM  ")
                print("   .JMML.    `'bmmd''    `bmmmmd''            VF      VF       `'bmmd'' .JML.    YM  ")

                break




    def hangman_graphic(self, guesses):
        if guesses == 0:
            print "              "
            print "              "
            print "              "
            print "              "
            print "              "
            print "              "
            print "--------------"
        elif guesses == 1:
            print "              "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
            print "--------------"
        elif guesses == 2:
            print "________      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
            print "--------------"
        elif guesses == 3:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
            print "--------------"
        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|             "
            print "|             "
            print "|             "
            print "--------------"
        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /       "
            print "|             "
            print "|             "
            print "--------------"
        elif guesses == 6:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|      "
            print "|             "
            print "|             "
            print "--------------"
        elif guesses == 7:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|             "
            print "|             "
            print "--------------"
        elif guesses == 8:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|     /       "
            print "|             "
            print "--------------"
        else:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|     / \     "
            print "|             "
            print "--------------"
            print G + "YOU LOST"
            print "GAME OVER!" + W
            self.__init__()

    def progress_updater(self, guess, the_word, progress):
        i = 0
        while i < len(the_word):
            if guess == the_word[i]:
                progress[i] = guess
                i += 1
            else:
                i += 1

        return "".join(progress)
