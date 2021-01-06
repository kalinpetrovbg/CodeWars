import string
alpha = string.ascii_lowercase

def position(alphabet):
    for num, index in enumerate(alpha):
        if index == alphabet:
            return f"Position of alphabet: {num + 1}"
