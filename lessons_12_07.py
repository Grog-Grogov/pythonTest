'''Практическое задание:
▫️Для примера с двумя аргументами написать обычную функцию add.
▫️Написать анонимную функцию, которая получает 4 аргумента и складывает их между собой. '''

def adds(a, b):  # Обычная функция
    print(a + b)

adds(1,5)

f = lambda x, y, z, w: x + y + z + w  # Анонимная функция
print(f(5, 6, 3, 9))

print('---------------------------------------------------------------------------------------------------')

#   рактическое задание:
#   1. Напишите декоратор, который вычисляет время выполнения функции.
#   2. Умножьте все элементы списка на 2 с помощью map и лямбды.
#   3. Из списка из чисел отфильтровать чётные числа.


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res
    return wrapper
print("Умножаем на два - [3, 7, 5, 2 , (-3), 3]")
lis = [3, 7, 5, 2 , (-3), 3]
print(list(map(lambda x: x * 2, lis)))

print("Фильтруем только чётные числа из списка  [-2, -1, 1, 2, 3, 4, 5, 66, 99 ,88 ,124]")
l1 = [-2, -1, 1, 2, 3, 34, 5, 66, 101 ,88 ,124]
print(list(filter(lambda x: not x % 2 , l1)))
print("Фильтруем  только не чётные числа из списка")
print(list(filter(lambda x:  x % 2 , l1)))





