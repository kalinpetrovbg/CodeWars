def spin_words(sentence):
    result = []
    alls = sentence.split()
    for word in alls:
        if len(word) >= 5:
            word = word[::-1]
        result.append(word)

    return " ".join(result)