import  time

def my_deco(sam_func):
    def wrapper(*args, **кwargs):
        t = time.time()
        print('код до функции')
        sam_func(*args, **кwargs)
        time.sleep(1) # задерка работы функции как пример
        print('время работы функции--', sam_func.__name__, time.time() - t) # время вычислениия работы функии
        print('Код после функции')
        return sam_func
    return wrapper


@my_deco
def list_prin(a, b):
    print('--sum---', a + b)

@my_deco
def func_2(a,b):
    print('------------', a + b)

@my_deco
def func_3(a):
    print('----',[4, 5, 6, 7, 8])



list_prin(4, 6)
func_2(4, 8)
func_3(2)


t = time.time()
print('время в настоящий момент', t)

lambada = list(map(lambda x: x * 2, range(6)))
print(lambada)

lambada_1 = list(filter(lambda x: x % 2==0, range(16)))
print('чЁтные числа из списка', lambada_1)
