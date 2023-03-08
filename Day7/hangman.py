import random
import hangman_words
import hangman_art

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
solution = [] # for the player's 'board'
lives = 6 # to display the hangman

print(chosen_word) # for pre-deployment testing

print(f"Your word has {word_length} letters in it.  ")

# to create the initial blanks '_'
for i in range(word_length):
    solution.append('_') # or could use solution += '_ '
print(''.join(solution))

end_of_game = False
while not end_of_game:
    guess = input("Ready! Pick a letter: ").lower()
    if guess in solution:
      print(f"You have already guessed '{guess}'")

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            solution[position] = letter
    
    if guess not in chosen_word:
      print(f"You guessed '{guess}' which is not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print(f"You lose!, the word was {chosen_word}") 

    print(f"{' '.join(solution)}")

    if '_' not in solution:
        end_of_game = True
        print("You win!")
    
    print(hangman_art.stages[lives])

