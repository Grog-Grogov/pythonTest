def bank():
    print('введите сумму для вклада в банк')
    s = int(input())  # Сумма вклада
    print(' введите ставку')
    p = float(input())  # Процентная ставка
    print('введите колличество лет')
    n = int(input())  # Колличество месяцев
    for i in range(1, n + 1):
        asd = s * (1 + p / 100) ** i
    if  i  == 1:
        print('За', i, 'год - доход по вкладу', asd)
    elif 2 <= i < 5:
        print('За', i, 'года - доход по вкладу', asd)
    elif i > 5:
        print('За', i, 'лет - доход по вкладу', asd)

bank()