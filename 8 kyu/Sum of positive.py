def positive_sum(arr):
    result = 0
    for x in arr:
        if x > 0:
            result += x
    return result