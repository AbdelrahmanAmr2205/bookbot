import sys
from stats import count_words, get_char_stats, get_sorted_char_stats

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path= sys.argv[1]
    book_contents= get_book_text(file_path)
    num_words= count_words(book_contents)
    char_stats= get_char_stats(book_contents)
    sorted_char_stats= get_sorted_char_stats(char_stats)
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {file_path}...")
    print("-" * 11 + " Word Count " + "-" * 11)
    print(f"Found {num_words} total words")
    print("-" * 9 + " Character Count " + "-" * 9)
    for char_stat in sorted_char_stats:
        char= char_stat["char"]
        count= char_stat["count"]
        if char.isalpha():
            print(f"{char}: {count}")
        else:
            continue
    print("============= END ===============")

main()
