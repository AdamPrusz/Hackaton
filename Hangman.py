# Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
# Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
# Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
# W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.


game = {
    "IT language": "python",
    "city": "berlin",
    "brand": "samsung",
 }

category = input("choose you category, IT language, city or brand': ")

word = game[category]

print("Password has: ", len(word), "letters")


current_word = "_" * len(word)
current_word = list(current_word)

print("You can make only 5 mistakes")
letter = input("Guess the letter: ")

mistakes = 0


while word:
    if letter in word:
        print ("CORRECT!")
        for index in range(len(current_word)):
            if letter == word[index]:
                current_word[index] = letter
            else:
                continue
        print(" ".join(current_word))
        letter = input("Guess the another letter, or guess the full word: ")
    elif letter not in word:
        mistakes = mistakes + 1
        print("Not correct, numbers of your mistake is: ", mistakes)
        print(" ".join(current_word))
        if mistakes < 5:
            letter = input("Guess the another letter, or guess the full word: ")
        else:
            print("GAME OVER")
            print("The word is: ", word)
            break
    if letter == word:
        print("CONGRATS! YOU WON")
        print("The word is: ", word)
        break













