import sys 
if len(sys.argv) != 2:
    print("Usage: python3 main.py <target_file>")
    sys.exit(1)

target_file = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import wordcount

from stats import charcount

from stats import sort_dict

def main():
    
    words = get_book_text(target_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {target_file}")
    print("----------- Word Count ----------")
    
    print(f"Found {wordcount(words)} total words")
    
    print("--------- Character Count -------")
    
    char_counts = charcount(words)

    sorted_chars = sort_dict(char_counts)
    for item in sorted_chars:
        char = item["char"]
        count = item["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")

    print("============= END ===============")


main()

    