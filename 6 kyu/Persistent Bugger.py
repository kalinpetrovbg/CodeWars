def persistence(n):
    new = []
    result = 1
    n = str(n)
    while len(n) > 1:
        for index in range(len(n)):
            result *= int(n[index])
        n = str(result)
        result = 1
        new.append(n)
    return len(new)