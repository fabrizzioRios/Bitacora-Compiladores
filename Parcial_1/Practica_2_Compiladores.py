import re

RESERVED_WORDS = ["digit", "bool", "text", "hw", "SI",
                  "O", "PARA", "camBIO", "endALL", "=>",
                  "mas", "menos", "mult", "entre", "eq", ]

def main():
    menu_value = int(input(
        "Practica 2 - Compiladores - 24 de Enero del 2024\nSamuel Gutierrez Madrigal\nLuis Fabrizzio Rios Ruiz\n\n"
        "Bienvenido al programa, escoge lo que deseas hacer:\n\n"
        "1) Probar con nuestro propio lenguaje\n"
        "2) Introduce una cadea\n"
        "4) Salir"))
    if menu_value == 1:
        archive_decision = int(input("1)Prueba\n\n2)Salir"))
        if archive_decision == 1:
            archive_name = "sfpython.txt"
            archive_result_string = read_archive(archive_name)
            words_list = text_processing(archive_result_string)
            count_and_compare_words(words_list)
            main()
        if archive_decision == 2:
            main()
    if menu_value == 2:
        given_string = str(input("Dame una cadena:"))
        words_list = text_processing(given_string)
        count_and_compare_words(words_list)
        main()
    if menu_value == 3:
        exit()
    else:
        print("No es una opcion valida")
        main()


def read_archive(archive_name: str) -> str:
    with open(f"./text_archives/{archive_name}", "rb") as file:
        return file.read().decode('utf-8')


def text_processing(archive_result_string: str) -> list:
    erased_comments = re.sub("(\/\/.+?)(?=\r?\n|$)", "", archive_result_string)
    return re.findall("([a-zA-Z\=\>]+)", erased_comments)


def count_and_compare_words(words_list: list) -> None:
    word_count = {}
    for item in words_list:
        if item in word_count:
            word_count[item] += 1
        else:
            word_count[item] = 1
    for word, count in word_count.items():
        if word in RESERVED_WORDS:
            print(word, "=", count)


if __name__ == '__main__':
    main()
