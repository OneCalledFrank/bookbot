import sys
from stats import count_words, count_characters, convert_sort  



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = count_words(text)
    characters = count_characters(text)
    ordered_list = convert_sort(characters)
    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in ordered_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
