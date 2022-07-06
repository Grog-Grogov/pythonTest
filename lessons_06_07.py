
a = [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]
def num_5(a):
     for i in a:
       if  i < 5: print(i)  #
num_5(a)
print()

list_1 = [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]
list_2 = [1, 2, 1, 2, 101, 7, 43, 9, 10, -1, 0]
'''main_list = list(set(list_1) - set(list_2))
main_list.sort()
print(main_list)  #Выводит значение 1 лист которых нет во втором отсортированное
'''
print()

x1 = [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]
y2 = [1, 2, 1, 2, 101, 7, 43, 9, 10, -1, 0]

def list_znach(x, y):
    main_list = list(set(x) - set(y))
    return(main_list)
print(list_znach(x1,y2))

list_znach(x1,y2)

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

'''my_dict1 = {'12':500, '22':5874, '33': 560, '44':400, '95':5874, '66': 20}
print(max(my_dict.values())) #Выводит MAX значение
print(max(my_dict1))         #Выводит MAX ключ
'''

def max_vol(a):
    print(max(my_dict.values()))
max_vol(my_dict)

