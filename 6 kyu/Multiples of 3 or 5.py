def solution(number):
    total = 0
    for x in range(1, number):
        if x % 3 == 0:
            total += x
            continue
        elif x % 5 == 0:
            total += x
    return total
