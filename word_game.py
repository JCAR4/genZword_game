import random

word_bank = ['rizz', 'bet', 'sus', 'yeet', 'cap', 'slay', 'vibe', 'gyatt', 'skibidi',
    'sigma', 'ohio', 'drip', 'bussin', 'fam', 'lowkey', 'mid', 'delulu', 
    'lit', 'npc', 'goat']

word = random.choice(word_bank)
guessword = ['_'] * len(word)
attempts = 10

print("🎯 Welcome to the Gen Z Word Guesser! Type one letter at a time.")

while attempts > 0:
    print("\nCurrent word: " + " ".join(guessword))
    guess = input("Your guess: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessword[i] = guess
        print("🔥 Big W! You ate that.")
    else:
        attempts -= 1
        print("💀 L move, fam. Attempts left:", attempts)

    if '_' not in guessword:
        print("\n🌟 W in the chat! You guessed it, the word is: " + word)
        break

if attempts == 0:
    print("\n☠️ No cap, you lost. The word was: " + word)
