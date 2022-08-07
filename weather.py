import sys
import requests
def get_weather():
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    city = sys.argv[0]
    params = { 'key': '99b5b9c68c19499db87211044220508',
               'q': city,
               'format': 'json',
               'num_of_days': 1,
               'lang': 'ru'}
    r = requests.get(url, params=params)
    the_weather = r.json()
    # данной строкой мы преобразуем полученное содержимое страницы
    # в формат json, который очень похож на тип данных dict() в Python
    # и с которым очень удобно работать
    if 'data' in the_weather:
        if 'current_condition' in the_weather['data']:
            try:
                return the_weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return 'Server Error'
    return 'Server Error'


if __name__ == '__main__':
    weather = get_weather()
    print(f'Погода сейчас {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}')


print('______________________________________')
