f = open('price.txt')
price = 0
for i in f:
    i = i.split('\t')
    price += eval(i[2]) * eval(i[1])
print(price)
