def read_book(title_path):
    with open(title_path) as f:
        file_contents = f.read()
        print(file_contents)


def main():
    read_book("books/frankenstein.txt")


main()

