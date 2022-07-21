from collections.abc import Hashable
list_1 = [5, 4.6, 8, [1, 'd'], ('s', [3, 2], ), 'abc', 'l']
set_1 = {item for item in list_1 if isinstance(item, Hashable)}
print(set_1)
