import string

def alphabet_position(text):
    result = []
    text = text.lower()
    alphabet = string.ascii_lowercase
    for letter in text:
        for num, each in enumerate(alphabet):
            if letter == " ":
                continue
            if letter == each:
                result.append(str(num + 1))
    return " ".join(result)