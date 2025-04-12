def count_words(book):
    return len(book.split())

def character_count(book):
    num_characters = {}
    for character in book:
        lower_char = character.lower()
        if lower_char in num_characters:
            num_characters[lower_char] += 1
        else:
            num_characters[lower_char] = 1

    return num_characters

def sort_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char" : char, "count" : count})

    def sort_on(dict_item):
        return dict_item["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    