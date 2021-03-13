# Wisielec:
# Program, będący implementacją gry "wisielec".
#
# Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
# Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
# Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
# W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.
# Popraw kod wisielca, tak by pobierać hasła do gry z pliku hangman.json. Plik powinnien zawierać conamniej jedno
# zagnieżdżenie odpowiadające kategoriom, które użytkownik może wybrać w grze. Kategorie pobrane z pliku JSON pojawiają
# się jako elementy menu start.


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


letter = input("Guess the letter: ")

mistakes = 0


while word:
    if letter in word:
        print ("CORRECT!")
        index_letter = word.index(letter)
        current_word[index_letter] = letter
        print(" ".join(current_word))
        letter = input("Guess the another letter, or guess the full word: ")
    elif letter not in word:
        mistakes = mistakes + 1
        print("Not correct, numbers of your mistake is: ", mistakes)
        print(" ".join(current_word))
        letter = input("Guess the another letter, or guess the full word: ")
    if letter == word:
        print("CONGRATS! YOU WON")
        print("The word is: ", word)
        break
    if mistakes == 5:
        print("GAME OVER, YOU LOSE")
        break











