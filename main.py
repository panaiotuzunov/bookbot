from stats import count_words, get_character_occurrence, chars_dict_to_sorted_list
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_contents = get_file_contents(path)
    characters_dict = get_character_occurrence(file_contents)
    sorted_list = chars_dict_to_sorted_list(characters_dict)
    print_report(path, file_contents, sorted_list)


def get_file_contents(path):
    with open(path) as f:
        return f.read()


def print_report(path, text, sorted_list):
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(text)} words found in the document")
    print()

    for dict in sorted_list:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")
            # print(f"The {dict["char"]} character was found {dict["num"]} times")
    print("--- End report ---")


main()