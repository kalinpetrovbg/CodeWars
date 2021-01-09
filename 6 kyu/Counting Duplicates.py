def duplicate_count(text):
    new_word = []
    uniques = []
    text = text.lower()
    for letter in text:
        if letter not in new_word:
            new_word.append(letter)
        else:
            uniques.append(letter)
    return len(set(uniques))