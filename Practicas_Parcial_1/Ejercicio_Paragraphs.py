
def main() -> None:
    archive_name = "apocalipsis.txt"
    archive_result_string = read_archive(archive_name)
    paragraph_list = count_paragraphs(archive_result_string)
    words_list = count_words(archive_result_string)
    print(count_characters(paragraph_list))


def read_archive(archive_name: str) -> str:
    with open(f"./text_archives/{archive_name}", "rb") as file:
        return file.read().decode('utf-8')


def count_paragraphs(text: str) -> list:
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    num_paragraphs = len(paragraphs)
    print(num_paragraphs)
    return paragraphs


def count_words(text: str) -> list:
    num_words = text.split(' ')
    print(len(num_words))
    return num_words


def count_characters(words_list: list) -> int:
    amount_characters = 0

    for element in words_list:
        amount_characters = amount_characters + len(element)
    return amount_characters


if __name__ == '__main__':
    main()
