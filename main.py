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
    return char_dict


def strip_non_alpha(characters):
    characters_without_symbols = {}

    for char in characters:
        if char.isalpha():
            characters_without_symbols[char] = characters[char]
    return characters_without_symbols


def dict_to_list(dict_obj):
    return [{"char": key, "count": value} for key, value in dict_obj.items()]


def main():
    path = "books/frankenstein.txt"
    print(f"--- Begin report of {path} ---\n")

    text = read_book(path)

    words = count_words(text)
    print(f"There are { words } words in this book.\n")

    print("Character count:")

    characters = count_characters(text)
    characters_without_symbols = strip_non_alpha(characters)

    char_list = dict_to_list(characters_without_symbols)
    char_list.sort(key=lambda x: x["count"], reverse=True)
    for item in char_list:
        print(f"{item['char']} : {item['count']}")


main()
