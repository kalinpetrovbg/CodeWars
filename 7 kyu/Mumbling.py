def accum(s):
    new_list = []
    for index in range(len(s)):
        result = s[index].upper() + s[index].lower() * index
        new_list.append(result)
    return "-".join(new_list)

