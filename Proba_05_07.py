def poisk(*args):
    print("Напишите предложение, не менее 20 символов.")
    add = input("")
    print('вставте символ для посика в вашем предложении.')
    add1 = input("")
    print(' ввашем предложении нашлось', add.count(add1), add1,'символов')
    return args
poisk()