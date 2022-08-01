

def my_fun(a):
    l1 = []
    for i in a:
        l1.append(i * 5)
    return l1
b = [3, 5, 7, 'class - ']
qwert = my_fun(b)
print(qwert)

asd = [09.98, 565, 'fgg']
def my_func_1(a):
    print(a)
a_1 = my_func_1(asd)

def my_func_2(a=1):
    print('Функция c 1 необязательным ',a)
asd_2 = my_func_2()
print(asd_2)

def my_func_3(*args):
    print('c переменным количеством позиционных аргументо',args)
my_func_3(2, 4, 'oops')
#print(my_func_3())

def my_func_4(**кwargs):
    print (кwargs)
my_func_4( aa = 234, fix = 4353 )
#print('Функция c переменным количеством именованных аргументов', my_func_4())

def my_func_5(*args, **кwargs):
    print (args, кwargs)
my_func_5(4, 77, 'qwerty', a = 4, b = 7)

my_list = (9, 8, 7, 6, 5)
my_dict = [1, 2, 3, 4]
for i in my_list:
    print('----', i)
for i in my_dict:
    print('*', i)
a = [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]
for i in a:
    if i < 5:
        print('----', i)

print("================++++++=====")


my_dict = {'a':500, 'b':5674, 'c': 560,'d':400, 'e':5874, 'f': 20}
def maxfun(a):
    print('самое большое значение -', max(my_dict.values()))
maxfun(my_dict)

def my_dickttt():
    for i in my_dict:
       print(my_dict.values())

a = [1, 1, 2, 3, 5, 7, 8, 99, 101, 21, 3]
b = [1, 2, 1, 2, 101, 7, 43, 9, 10, -1, 0]


def my_fun_123(x, y):
    i = 0
    while i < len(x):
        for l in y:
            if l == x[i]:
                x.remove(l)
        i = i + 1
    print('работает while  ', x)
    print("=====================")

my_fun_123(a, b)
