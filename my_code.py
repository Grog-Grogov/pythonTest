def my_func(a):
    print(a)
    for i in a:
        print(i)
    return a
#d = {'family': 'Сидоров', 'name':'Ivan', 'Otchestvo':'Genadyvich'} # Слварь
dc = ['Bvz', 'dtavo', 'cwa']                                       # список
b = my_func(dc)


print ('Введите 3 числа')
m = int(input())
print(float(input()))
n = int(input())
for i in range(1,n+1):
    print(i, m)
    m=m+(m)