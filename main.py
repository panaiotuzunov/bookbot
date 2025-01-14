def main():
    path = "books/frankenstein.txt"
    file_contents = get_file_contents(path)

    print(f"--- Begin report of {path} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()
    print_character_occurrence(file_contents)
    print("--- End report ---")


def get_file_contents(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    counter = 0
    words = text.split()
    return len(words)


def character_occurrence(text):
    occurrences = {}
    text_lower = text.lower()
    for character in text_lower:
        if character in occurrences:
            occurrences[character] += 1
        else:
            occurrences[character] = 1
    return occurrences


def print_character_occurrence(text):
    pass

main()