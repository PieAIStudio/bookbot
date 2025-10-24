from stats import get_book_text, count_words, count_characters, sort_character_counts
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    num_words = count_words(get_book_text(sys.argv[1]))
    char_counts = count_characters(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    sort_character_counts(char_counts)
    print("============= END ===============")
main()