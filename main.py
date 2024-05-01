import os
import random
from hangman_art import hangman
from hangman_words import word_list






random_soz = random.choice(word_list)

display = []
level = 6

word_len = len(random_soz)
for _ in range(word_len):
    display += "_"
print(display)

end_of_game = False

print("""
_                                             
| |                                            
| |__ __ _ __ __ _ _ ___ __ _ _ _ _ _________ 
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |).
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ """)

while not end_of_game:
    tahmin = input("Tahminiy xarfni kiriting: ").lower()
    os.system("cls")

    if tahmin in display:
        print(f"Bu xarfdan foydalandingiz {tahmin}")

    for position in range(word_len):
        letter = random_soz[position]
        if letter == tahmin:
            display[position] = letter


    if tahmin not in random_soz:
        print(f"Siz ushbu xatni taxmin qildingiz {tahmin}")
        level -= 1
        if level == 0:
            end_of_game = True
            print("Siz yutqazdingiz!")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Siz g'olipsiz!")
        

    print(hangman[level])
    
