def filter_list(l):
    return [x for x in l if type(x) != str]

# Old solution
#     new = []
#     for x in l:
#         try:
#             if x >= 0:
#                 new.append(x)
#         except:
#             pass
#     return