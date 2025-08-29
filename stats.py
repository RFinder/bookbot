# Wortzahl wird bestimmt
def get_num_words(text):
    word_list = text.split() # Text wird in Liste mit Worten geteilt
    word_count = len(word_list) # Anzahl Einträge in Liste
    return word_count

# Zeichenanzahl aus Text wird gezählt und in Dict geschrieben (nur Kleinbuchstaben)
def get_num_letters(text):
    dict_letters ={}
    text_small = text.lower() # Transformation in Kleinbuchstaben
    for letter in text_small: # Jedes Zeichen im Text wird durchlaufen
        if letter in dict_letters: # Vorhandene Keys -> Update | Neuer Key -> Hinzufügen
            dict_letters[letter] += 1
        else:
            dict_letters[letter] = 1
    return dict_letters

# Rückgabe des Keys für Sortierung
def sort_on(items):
    return items["num"]

# Erzeugen einer sortierten List of Dicts
def sort_dictionary(letter_count):
    letter_sort = []
    for key in letter_count:
        dict_entry = {}
        dict_entry["char"] = key
        dict_entry["num"] = letter_count[key]
        letter_sort.append(dict_entry)
    letter_sort.sort(reverse=True, key=sort_on) # Liste nach Häufigkeit sortieren und zurückgeben
    return letter_sort