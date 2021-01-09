def move_zeros(array):
    qty = array.count(0)
    for _ in range(qty):
        array.remove(0)
        array.append(0)
    return array


# to be sorted out with print(move_zeros([1, None, 2, 1, 0, 0, 0]))