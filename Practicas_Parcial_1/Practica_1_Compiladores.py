import re


def main():
    menu_value = int(input(
        "Practica 1 - Compiladores - 11 de Enero del 2024\nSamuel Gutierrez Madrigal\nLuis Fabrizzio Rios Ruiz\n\n"
        "Bienvenido al programa, escoge lo que deseas hacer:\n\n"
        "1) Introducir el nombre del archivo\n"
        "2) Escoger entre la lista de archivos\n"
        "3) Introduce un string\n"
        "4) Salir"))
    if menu_value == 1:
        archive_name = str(input("Nombre del archivo"))
        archive_result_string = read_archive(archive_name)
        words_list = text_processing(archive_result_string)
        count_and_compare_words(words_list)
        main()
    if menu_value == 2:
        archive_decision = int(input("1) Proverbios\n\n2) Ezequiel\n\n3) Apocalipsis\n\n4) Salir"))
        if archive_decision == 1:
            archive_name = "proverbios.txt"
            archive_result_string = read_archive(archive_name)
            words_list = text_processing(archive_result_string)
            count_and_compare_words(words_list)
            main()
        if archive_decision == 2:
            archive_name = "ezequiel.txt"
            archive_result_string = read_archive(archive_name)
            words_list = text_processing(archive_result_string)
            count_and_compare_words(words_list)
            main()
        if archive_decision == 3:
            archive_name = "apocalipsis.txt"
            archive_result_string = read_archive(archive_name)
            words_list = text_processing(archive_result_string)
            count_and_compare_words(words_list)
            main()
        if archive_decision == 4:
            main()
    if menu_value == 3:
        given_string = str(input("Give me a string:"))
        words_list = text_processing(given_string)
        count_and_compare_words(words_list)
        main()
    if menu_value == 4:
        exit()
    else:
        print("No es una opcion valida")
        main()


def read_archive(archive_name: str) -> str:
    with open(f"./text_archives/{archive_name}", "rb") as file:
        return file.read().decode('utf-8')


def text_processing(archive_result_string: str) -> list:
    erased_comments = re.sub("(\/\/.+?)(?=\r?\n|$)", "", archive_result_string)
    return re.findall("([a-zA-Z]+)", erased_comments)


def count_and_compare_words(words_list: list) -> None:
    word_count = {}
    for item in words_list:
        if item in word_count:
            word_count[item] += 1
        else:
            word_count[item] = 1
    for word, count in word_count.items():
        print(word, "=", count)


if __name__ == '__main__':
    main()
