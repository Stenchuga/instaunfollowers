import random

hidden_word_display = []   # crticee -> lista koja prikazuje trenutno otkrivene/slobodne pozicije
lives = 6                  # zivoti -> broj preostalih života
word_list = ['Danica', 'Aleksa', 'Dragan']  # reci -> lista reči

chosen_word = str(random.choice(word_list)) # rec -> nasumično izabrana reč
word_length = len(chosen_word)              # crtice -> broj slova u reči

for i in range(word_length):
    hidden_word_display.append('_')

print("Welcome to Hangman")
print(''.join(hidden_word_display))

while lives > 0:
    guess_letter = input("Guess a letter: ")

    if guess_letter in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess_letter:
                hidden_word_display[index] = guess_letter

        current_guess_state = ''.join(hidden_word_display)
        print(current_guess_state)

        if current_guess_state == chosen_word:
            print('You won!')
            break
    else:
        if lives > 0:
            lives -= 1
            print(f'That letter is not in the word.\nYou have {lives} lives left.')
            if lives == 5:
                print('Lost the head')
            elif lives == 4:
                print('Lost the body')
            elif lives == 3:
                print('Lost one arm')
            elif lives == 2:
                print('Lost the other arm')
            elif lives == 1:
                print('Lost one leg')
        elif lives == 0:
            print("You lost!")


