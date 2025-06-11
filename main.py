import sys

from stats import get_num_chars, get_num_words, sort_char_dict


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    for entry in sort_char_dict(get_num_chars(get_book_text(sys.argv[1]))):
        if entry["name"].isalpha():
            print(f"{entry["name"]}: {entry["num"]}")
    print("============= END ===============")


main()
