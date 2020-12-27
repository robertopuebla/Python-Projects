import random
print('H A N G M A N')
word_bank = ['python', 'java', 'kotlin', 'javascript']
letters_used = []
answer: str = random.choice(word_bank)
letters = list(answer)
word_display = '-' * len(answer)
display_list = list(word_display)
tries = 8


def menu():
    intro = input('Type "play" to play the game, "exit" to quit: ')
    if intro == 'play':
        play()
    else:
        exit()


def play():
    global tries
    global word_display
    while tries > 0:
        print()
        print(word_display)
        if '-' not in word_display:
            print('You guessed the word.')
            print('You survived!')
            menu()
        elif tries == 0 and '-' in answer:
            print('You lost!')
            menu()
        else:
            player_input = input("Input a letter: ")
            if player_input in letters_used:
                print("You've already guessed this letter")
            elif len(player_input) != 1:
                print('You should input a single letter')
            elif player_input.islower() is False or player_input.isalpha() is False:
                print('Please enter a lowercase English letter')
            elif player_input in answer:
                letters_used.append(player_input)
                indices = [z for z, x in enumerate(letters) if x == player_input]
                for n in indices:
                    display_list[int(n)] = player_input
                    word_display = "".join(display_list)
            else:
                print("That letter doesn't appear in the word")
                letters_used.append(player_input)
                tries -= 1
                if tries == 0:
                    print('You lost!')
                    menu()


menu()
play()
