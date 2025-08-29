# Import von statistiscchen Funktionen
from stats import get_num_words
from stats import get_num_letters


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    #get_num_words(book_text)
    get_num_letters(book_text)
    

main()