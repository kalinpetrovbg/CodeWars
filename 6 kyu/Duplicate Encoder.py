def duplicate_encode(word):
    word = word.lower()
    result = ""
    for letter in word:
        if word.count(letter) == 1:
            result += "("
        else:
            result += ")"
    return result