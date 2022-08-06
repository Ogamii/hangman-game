import random


def word_choice():
    keys = []
    values = []
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        values = [line.replace("\n","") for line in f]
        num_words = len(values)
        keys = [i for i in range(1, num_words+1)]
    word_list = {keys[i]: values[i] for i in range(0, num_words) }
    random_key = random.randint(0,num_words-1)
    random_word =word_list[random_key]
    return random_word
    


def run():
    print(word_choice())


if __name__ == '__main__':
    run()