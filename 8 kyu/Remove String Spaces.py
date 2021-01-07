def no_space(x):
    result = [letter for letter in x if letter != " "]
    return "".join(result)