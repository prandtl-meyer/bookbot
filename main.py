import sys
from stats import count_words, count_each_character, sort_dictionary

def get_book_text(bookpath):
    # This function reads a book from a given path and returns its text as a string.
    with open(bookpath) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    # This is the main function that runs the program.

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_text = get_book_text(sys.argv[1])  # Get the text of the book
    num_words = count_words(book_text)  # Count the words in the book text
    print(f"Found {num_words} total words")  # Print the word count
    char_count = count_each_character(book_text)  # Count each character in the book text
    
    for item in sort_dictionary(char_count):
        if item["char"].isalpha():
            print (f"{item['char']}: {item['num']}")  # Print the character and its count

main()