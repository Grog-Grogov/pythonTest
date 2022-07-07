
def my_func1(a):
    print(a)
    return a+1
my_func1(2)
print(sep='******************************************************************************')
def my_func2(a=1):
        print(a)
my_func2(23)
print(sep='******************************************************************************')
def my_func3(*args):
    print(args)
    return args
my_func3(1, 2, 3, 'abc')
print(sep='******************************************************************************')
def my_func4(**кwargs):
    print(кwargs)
    return кwargs
my_func4(a=1, b=2, c=3)
print(sep='******************************************************************************')
def my_func5(*args, **кwargs):
    print(args, кwargs)
    return args, кwargs
my_func5(1, 2, 3, 'abc', a=1, b=2, c=3)
print(sep='******************************************************************************')

def poisk(*args):
    print("Напишите предложение, не менее 20 символов.")
    add = input("")
    print('вставте символ для посика в вашем предложении.')
    add1 = input("")
    print(' ввашем предложении нашлось', add.count(add1), add1,'символов')
    return args
poisk()

print(sep='******************************************************************************')

print('Введите сумму вклада на 4 года под 10% годовых')
asd = float(input())
proc = 0.1
def vklad():
        a = (asd * proc) + (asd)
        return(a)
print(vklad(), 'первый год с процентами ')
a2 = (vklad() * proc) + vklad()
print(a2, 'второй год')
a3 = ((a2 * proc) + a2)
print(a3, 'третий год')
a4 = ((a3 * proc) + a3)
print(a4, 'четвертый год')

print('введите суммы, ставку и колличество лет')
s = int(input())  #Сумма вклада
p = float(input())  #Процентная ставка
n = int(input())    #Колличество месяцев
for i in range(n):
   asd = s * (1 + p/100)**i
   print(i + 1, asd)