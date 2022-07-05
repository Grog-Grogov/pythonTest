print(4 > 5), print(4 == 5), print(4 < 5)    # Bool type
a = 10                                       # integers type
b = 123.23                                   # float
c = 4 + 5j                                   # complex type
d = 'Строчный тип данных'                    # str type
e = ('ip', 123, 789, 23, 7)                  # tuple кортеж
f = {'name':'first', 'family':'second' }     # dict словарь
g = ['a', 'b', 'c', 56, {'name':'first', 'family':'second' }, ('кортежи')] # list списки
h = {3, 4, 5, 6, 7}                          #set множества
print(a, b, c, d, e, f, g, h, sep='\n')

print(end='--------------------------------------------------------------------------\n')

a1 = ('ШаЛаШ')
b1 = ('мадам')
a11 = a1[::-1]
b11 = b1[::-1]
if a1 >= a11 and b1 <= b11:
    print(a11, '-- Палиндром', 'и', b11, ' Тоже Палиндром')
else:
    print(" - Палиндром не обнаружен")

print(end='--------------------------------------------------------------------------\n')

list_first = [1, 3, 6.4, "последний элемент в списке"]
print(list_first[0], 'и ', list_first[-1])

print(end='--------------------------------------------------------------------------\n')

abc = [2, 4, 5, 7, 8, 10, 123, 20, 40]
for i in abc:
    if i % 2 == 0:
     print(i)
    elif i == 123:
        print('exit')
        break

print(end='--------------------------------------------------------------------------\n')

'''while True:
    command = input('ВВедите цифру один')
    if command == "1":
        user_text = str(input("Введите текст"))
        otvet = len(user_text)
        print('Количество символов', otvet)
    elif command == "/somvol":
        user_text = str(input("Введите текст")).split('о')
        otvet = len(user_text)
        print('Количество символов', otvet)
'''

command = input('ВВедите цифру один')
if command == "1":
    user_text = str(input("Введите текст "))
    otvet = len(user_text)
    print('Количество символов', otvet)






