list_1 = [1, 5, 8, 7, 10, 9, 7, 12, 8, 3, 6, 10, 3, 10, 10, 7, 3, 3, 3]
set_res = set()
for item in list_1:
    if item not in set_res:
        set_res.add(item)
    else:
        set_res.add(str(item) + str(item))
print(set_res)
