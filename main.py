import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = count_words(text)

        character_dict = count_characters(text)
        sorted_characters_list = sort_characters(character_dict)
        sorted_characters_list.sort(reverse=True, key=sort_on)


        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for item in sorted_characters_list:
            if item['char'].isalpha():
                print(f"{item['char']}: {item['num']}")
        
        print("============= END ===============")


main()
