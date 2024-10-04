import random
import hangman_art
import hangman_words
import os
end_of_game = False
logo = hangman_art.logo
print(logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    if guess in display:
        print(f"You've alredy guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.You lose a life.")
        lives -= 1
        if lives ==0:
            end_of_game=True
            print("You Lose..")
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])