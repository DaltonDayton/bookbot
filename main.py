def read_book(title_path):
    with open(title_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def main():
    text = read_book("books/frankenstein.txt")
    print(text)

    words = count_words(text)
    print(words)


main()
