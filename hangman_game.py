import random
import os
import pyfiglet


def normalize(s):
    replacements =""
    replacements = replacements.maketrans("áéíóú","aeiou")
    s = s.translate(replacements)
    return s


def word_choice():
    keys = []
    values = []
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        values = [line.replace("\n","") for line in f]
        num_words = len(values)
        keys = [i for i in range(1, num_words+1)]
    word_list = {keys[i]: values[i] for i in range(0, num_words) }
    random_key = random.randint(0,num_words-1)
    random_word = normalize(word_list.get(random_key))
    return random_word


def autofill():
    f = 0
    state = True
    word = list(word_choice())
    num_letters = len(word)
    message = list("_" * num_letters)
    while f <= 6 and state == True:
        letter_count = 0
        if message.count("_") != 0:
            try:
                letter = input("Ingresa una letra (exit para salir): ")
                if letter == "exit":
                    break
                elif letter.isalpha() != True:
                    raise TypeError("Ingresar solo letras")
                elif len(letter) != 1:
                    raise TypeError("Debe ingresar una y solo una letra")
                for i in range(0,num_letters):
                    if letter == word[i]:
                        message[i] = letter
                        letter_count += 1
                if letter_count == 0:
                    f += 1
                os.system("cls")
                draw(f)
                print("\n")
                print("".join(message))
            except TypeError as te:
                print(te)
                print("\n")                
        else:
                print(pyfiglet.figlet_format("¡¡Felicidades ganaste!!"))
                print("la palabra era: " + "".join(message))
                state = False 
    if f > 7 and state == True:
        draw(6)
        print(pyfiglet.figlet_format("Perdiste"))
        print("la palabra era: " + "".join(word))  


def draw(f):
    if f == 0: #Here starts the art
        print('''
 +----+
 |    |
      |
      |
      |
      |
=========''')
    elif f == 1:
        print('''
 +----+
 |    |
 O    |
      |
      |
      |
=========''')
    elif f == 2:
        print('''
 +----+
 |    |
 O    |
 |    |
      |
      |
=========''')
    elif f == 3:
        print('''
 +----+
 |    |
 O    |
/|    |
      |
      |
=========''')
    elif f == 4:
        print('''
 +----+
 |    |
 O    |
/|\   |
      |
      |
=========''')
    elif f == 5:
        print('''
 +----+
 |    |
 O    |
/|\   |
/     |
      |
=========''')
    elif f == 6:
        print('''
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
=========''')


def interface():
    os.system("cls")
    num_letters = len(word_choice())
    message = list("_" * num_letters)
    titulo = pyfiglet.figlet_format("HANGMAN  GAME")
    print(titulo)
    print("Adivina la palabra: ")
    print("".join(message))
    autofill()   


def run():
    interface()


if __name__ == '__main__':
    run()