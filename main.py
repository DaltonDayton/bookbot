def read_book(title_path):
    with open(title_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    words = text.split()
    char_dict = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return dict(sorted(char_dict.items()))


def main():
    text = read_book("books/frankenstein.txt")
    print(text)

    words = count_words(text)
    print(f"There are { words } words in this book.\n")

    print("The character counts in this book are: ")
    characters = count_characters(text)
    for char in characters:
        print(char, characters[char])


main()
