def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import wordcount

from stats import charcount

def main():
    words = get_book_text("./books/frankenstein.txt")
    print(f"{wordcount(words)} words found in the document")
    print(charcount(words))

main()

    