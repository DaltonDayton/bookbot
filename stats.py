def get_num_words(book_text):
    word_arry = book_text.split()
    return len(word_arry)


def get_num_chars(book_text):
    chars = {}
    for char in book_text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_on(dict):
    return dict["num"]


def sort_char_dict(char_dict):
    list_of_chars = []
    for char in char_dict:
        list_of_chars.append({"name": char, "num": char_dict[char]})
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars
