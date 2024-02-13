import random

lives = 6

from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

chosen_word = random.choice(word_list)

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in range(len(chosen_word)):
    display.append('_')

while '_' in display:
    guess = input('Guess a letter: ').lower()
    if guess in display:
        print(f'you\'ve already said that letter!')
    for i in range(len(chosen_word)):
        if guess in chosen_word[i]:
            display[i] = guess
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f'letter {guess} is not in word. you lose a life!')
        lives -= 1
    print(stages[lives])
    if lives == 0:
        print('oops, you lose...')
        break
    if '_' not in display:
        print('you won!!')
    


    

