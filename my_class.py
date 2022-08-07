class A:
    arg = 1
    def __init__(self, name):
        print(name)

    def my_metod(self):
        print('мой метод')

    def my_second(self):
        print('мой второй метод для закрепеления материала')





a = A(373)
a.my_metod() # вызов метода

b = A(543)
b.my_metod()   # вызов метода
b.my_second()   # вызов метода


c = A('-')
c.my_second()   # вызов метода

print(a.arg)
print(b.arg)
print(c.arg)






