print('Введите колличество потраченного ХВ')
a = float(input())
h = 50.86
print('Введите колличество потраченного ГВ')
g = 50.86
water_go = 55.06
b = float(input())
water_g = 55.06
water_power = 15.6
water_Cold = h * a
water_gorach = g * b
water_go_out = (a + b) * water_g
sum_water = water_Cold + water_gorach + water_go_out
water_power_gor = (10 * water_power) * b
sum_oplata = water_Cold + water_gorach + water_go_out + water_power_gor
print('Сумма за холодную воду', water_Cold)
print('Сумма за горячую воду', water_gorach)
print('Сумма за водоотведение', water_go_out)
print('Сумма за воду за исключением электричества на подогрев', sum_water)
print('Тепловая энергия на подогрев воды (индивидуальное потребление) ', water_power_gor)
print('Сумма Оплаты за воду ', sum_oplata)

