def to_jaden_case(string):
    str = []
    words = string.split()
    for letters in words:
        res = letters.capitalize()
        str.append(res)

    return " ".join(str)


# best solution:
def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())