import os, sys
from stats import count_words, character_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    num_words = count_words(contents)
    print(f"Found {num_words} total words")
    character_dict = character_count(contents)
    sorted_chars = sort_dict(character_dict)
    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['count']}") 

main()