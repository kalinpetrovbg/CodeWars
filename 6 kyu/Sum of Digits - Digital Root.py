def digital_root(n):
    while len(str(n)) > 1:
        n = sum(int(each) for each in str(n))
    return n