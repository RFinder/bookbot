# Wortzahl wird bestimmt
def get_num_words(text):
    word_list = text.split() # Text wird in Liste mit Worten geteilt
    word_count = len(word_list) # Anzahl Einträge in Liste
    print(f"{word_count} words found in the document")

# Zeichenanzahl aus Text wird gezählt und in Dict geschrieben (nur Kleinbuchstaben)
def get_num_letters(text):
    dict_letters ={}
    text_small = text.lower() # Transformation in Kleinbuchstaben
    for letter in text_small: # Jedes Zeichen im Text wird durchlaufen
        if letter in dict_letters: # Vorhandene Keys -> Update | Neuer Key -> Hinzufügen
            dict_letters[letter] += 1
        else:
            dict_letters[letter] = 1
    print(dict_letters)
