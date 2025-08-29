# Import sys-Modul
import sys
# Import von statistiscchen Funktionen
from stats import get_num_words
from stats import get_num_letters
from stats import sort_dictionary


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    # Abfangen, falls Systemeingabe nur 1 Argument hat
    try:
        book_path = sys.argv[1] # Buchpfad wird über Terminal eingegeben
    except IndexError:
        print("Second Argument is missing!")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Programm nach Fehlerausgabe beenden

    book_text = get_book_text(f"./{book_path}") # Buch in String einlesen
    word_count = get_num_words(book_text) # Wortanzahl bestimmen
    letter_dict = get_num_letters(book_text) # Buchstaben und Häufigkeit bestimmen
    letter_sort = sort_dictionary(letter_dict) # Sortieren nach Häufigkeit

    # Bericht in Console ausgeben
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Dict in List of Dicts transformieren und
    #  Buchstaben sortiert nach Häufigkeit ausgeben. 
    #e: 44538
    for item in letter_sort:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")



# Aufruf von MAIN
main()