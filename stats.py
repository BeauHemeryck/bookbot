def get_amount_of_word(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_amount_of_char(text):
    characters = list(text.lower())
    character_count = {}
    for char in characters:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count

def sort_dictionary(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))