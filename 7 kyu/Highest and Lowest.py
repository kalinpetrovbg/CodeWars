def high_and_low(numbers):
    l = [int(x) for x in numbers.split()]
    return f"{max(l)} {min(l)}"