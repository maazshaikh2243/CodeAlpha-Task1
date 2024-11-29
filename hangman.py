import random

def hangman_game():
    
    word_list = ["python", "hangman", "student", "learning", "coding"]
    word = random.choice(word_list)  
    guessed_word = ["_"] * len(word)  #_ _ _ _ _ _ _
    attempts_remaining = 7
    guessed_letters = []  
    print("\nWelcome to Hangman!")
    print("Your word to guess:", " ".join(guessed_word))

    while attempts_remaining > 0 and "_" in guessed_word:
        print(f"\nAttempts remaining: {attempts_remaining}")
        guess = input("Enter a letter: ").lower()

        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        
        if guess in guessed_letters:
            print("You already guessed that letter! Try another one.")   #st_ _ e n t t
            continue

        guessed_letters.append(guess)     

        if guess in word:
            print(f"Good job! '{guess}' is in the word.") #python p
            
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_remaining -= 1
            print(f"'{guess}' is not in the word.")

        print("Current word:", " ".join(guessed_word)) 

   
    if "_" not in guessed_word:  
       print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)


if __name__ == "__main__":
    hangman_game()
