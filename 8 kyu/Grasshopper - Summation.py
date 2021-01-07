def summation(num):
    total = 0
    for number in range(1, num + 1):
        total += number
    return total


print(summation(8))