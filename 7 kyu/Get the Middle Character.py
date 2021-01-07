def get_middle(s):
    middle = len(s) / 2
    middle = int(middle)
    if len(s) % 2 == 0:
        return s[middle - 1: middle + 1]
    else:
        return s[middle]
