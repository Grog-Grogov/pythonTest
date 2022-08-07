
class A:
    pass
a1 = A()
b = A()
c = A()

a1.arg = 1
b.arg = 2
c.arg = 33
print(a1.arg)
print(b.arg)
print(c.arg)
print(a1.arg + b.arg)


'''
class A3:
    def __init__(self, name, surname):
        self.name = name
a = A3("White Rabbit")
'''

class A_2:
    arg = "Alice"
    def __init__(self, name, surname):
        self.name = name
    def __my_private_method(self):
        print("just private")
    def my_method(self):
        print("Hello, ", self.name)


class A_4:
    arg = "Alice"

    def __init__(self, name, surname):
        self.name = name


def __my_private_method(self):
    print("just private")


def my_method(self):
    print("Hello, ", self.name)



class Circle:

    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return 3.1415 * self.r**2

c = Circle(10)
print(c.area)

class A1:
    def __init__(self):
        self.n = 10

    def total_a1(self, a):
        return self.n + int(a)


class A2:
    def __init__(self):
        self.n = 15

    def total_a2(self, a):
        return self.n + int(a)


class A3(A1, A2):

    def total_a3(self, a):
        return self.n + int(a)


a2 = A3()
print(a2.n)
print(a2.total_a3(1))


