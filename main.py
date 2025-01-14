def main():
    path = "books/frankenstein.txt"
    file_contents = get_file_contents(path)
    characters_dict = get_character_occurrence(file_contents)
    sorted_list = chars_dict_to_sorted_list(characters_dict)
    print_report(path, file_contents, sorted_list)
    


def get_file_contents(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    counter = 0
    words = text.split()
    return len(words)


def get_character_occurrence(text):
    occurrences = {}
    text_lower = text.lower()
    for character in text_lower:
        if character in occurrences:
            occurrences[character] += 1
        else:
            occurrences[character] = 1
    return occurrences


def print_report(path, text, sorted_list):
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(text)} words found in the document")
    print()

    #print character occurences 
    for dict in sorted_list:
        if dict["char"].isalpha() == True:
            print(f"The {dict["char"]} character was found {dict["num"]} times")

    print("--- End report ---")


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()