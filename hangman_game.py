import random


# def word_choice():
#     data = []
#     with open("./archivos/data.txt","r",encoding="utf-8") as f:
#         for line in f:
#             line = f.readline()
#             line = line.strip("\n")
#             data.append(line)
#         print(data)
#         print("\n")


def word_choice():
    data = []
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        for line in f:
            line = f.readline()
            line = line.strip("\n")
            data.append(line)
        word_list = list(map(lambda word: word,data))


if __name__ == '__main__':
    word_choice()