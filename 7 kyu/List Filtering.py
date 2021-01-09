def filter_list(l):
    new = []
    for x in l:
        try:
            if x >= 0:
                new.append(x)
        except:
            pass
    return 