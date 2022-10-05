# Напишите программу, которая бы «Подбрасывала» условную монету 100 раз и
# сообщала, сколько раз выпал орел, а сколько - решка.


from random import randint


COUNT_OF_THROWS = 100


def throw_coin():
    reshka_count = sum([randint(0, 1) for item in range(COUNT_OF_THROWS)])
    # for item in range(100):
    #     reshka_count += randint(0, 1)
    return COUNT_OF_THROWS - reshka_count, reshka_count


if __name__ == '__main__':
    eagle_count, tails_count = throw_coin()
    print(f'Количество орлов: {eagle_count}, количество решек: {tails_count}')
