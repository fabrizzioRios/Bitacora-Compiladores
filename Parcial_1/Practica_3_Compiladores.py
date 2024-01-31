import string

ALPHABET = list(string.ascii_letters)
DIGITS = list(string.digits)


def main() -> None:
    test_text = str(input("Practica 3 - Compiladores - 31 de Enero del 2024\n"
                          "Samuel Gutierrez Madrigal\n"
                          "Luis Fabrizzio Rios Ruiz\n\n"
                          "Introduce tu texto para validar"))
    state = 'A'
    for i in test_text:
        try:
            if state == 'A':
                if i in ALPHABET:
                    state = 'B'
                elif i == '_':
                    state = 'B'
                else:
                    raise Exception(f"No se esperaba: {i}")
            if state == 'B':
                if i in ALPHABET or i == '_' or i in DIGITS:
                    state = 'B'
                else:
                    raise Exception(f"No se esperaba: {i}")
            main()
        except Exception as error:
            print(error)
            main()


if __name__ == '__main__':
    main()
