list_1 = ['a', 'b', 'c', 'd']
list_2 = [1, 2, 3, 4]
dict_1 = {}
for item in range(len(list_1)):
    dict_1[list_1[item]] = list_2[item]
print(dict_1)
