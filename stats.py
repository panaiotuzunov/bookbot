def count_words(text):
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


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(dict):
    return dict["num"]