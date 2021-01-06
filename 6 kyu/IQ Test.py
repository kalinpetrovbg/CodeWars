def iq_test(numbers):
    even = []
    odd = []
    position1 = 0
    position2 = 0
    res = numbers.split()
    for pos, num in enumerate(res):
        num = int(num)
        if num % 2 == 0:
            even.append(num)
            position1 = pos
        else:
            odd.append(num)
            position2 = pos

    if len(even) < len(odd):
        return position1 + 1
    else:
        return position2 + 1
