list_1 = [22 , 44]
'''
for i in list_1:
    print(i * 2)
print(list_1)
'''

''''
list_2 = [x *2 for x in [21, 43, 'fix', 'lessons', 56 , 85, 993, 74, 45, 'hellow world']]
print(list_2)

list_3 = [x *2 for x in (list_1)]
print('списковое включение ', list_3)


list_4 = (x * 2 for x in (list_3))
for i in list_4:
  print('генератор',i)
'''
list_3 = [x *2 for x in (list_1)]
list_4 = (x *2 for x in (list_3))


try:
    print(next(list_4))
    raise Exception
    print(next(list_4))
    print(next(list_4))
    print(next(list_4))


except StopIteration:
   print('программа выполнена для конца')

except Exception:
    print('Пойман Exception')

finally:
   print('я доделаю всё равно ')

print('+++++++++++++++++++++++++++++++++')
list_4 = [x * 2 for x in (list_3)]
for i in list_4:
    print('генератор-==-', i)

list_1_1 = [1, 1, -1, 1]
def gen_fun():
    for i in list_1_1:
        if i >= 0:
            yield i * 0
        print('----- ')
        yield i * 3
        yield i * 5
        yield i + 7
for item in gen_fun():
  print(item)

print('++++++++++++++++++++++++++++++++++++++++++++++++')

gen_0 = (1, -8, -8, 8, 0, 86)
gen_asd = (x * 0 for x in gen_0 if x >= 0)
for i in gen_asd:
  print('зануляем положительные числа', i)








