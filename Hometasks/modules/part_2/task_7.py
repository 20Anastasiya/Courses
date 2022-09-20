"""
7. Напишите программу для поиска наиболее распространенных элементов и их количества в указанном тексте.
"""


from collections import Counter


sentense = 'This is my new task for homework. Topic - libraries'
print(Counter(sentense))
