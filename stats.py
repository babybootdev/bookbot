def count_words(book: str) -> str:
    total_words = len(book.split())
    return total_words

def count_characters(book: str) -> dict:
    book = book.lower()
    character_counts = {}

    for char in book:
        if char not in character_counts:
            character_counts[char] = 1
        else:
            character_counts[char] += 1
    return character_counts

def sort_characters(characters: dict) -> list:
    sorted_list = []

    for char in characters:
        sorted_list.append({"char": char,
                            "num": characters[char]})
    return sorted_list
