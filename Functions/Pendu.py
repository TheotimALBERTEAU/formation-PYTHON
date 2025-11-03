def Pendu(word_to_find):
    word_to_find_backup = word_to_find
    attempts = 0
    letters = []
    while word_to_find != "":
        letter = input("Enter a letter to find the Pendu: ")
        if letter not in letters:
            attempts += 1
            for i in word_to_find:
                if letter == i:
                    word_to_find = word_to_find.replace(letter, '')
        else:
            print("Letter already proposed")
        letters.append(letter)
    print("Tu as trouvé toutes les lettres du mot en", attempts, "essais")
    print("le mot était", word_to_find_backup)