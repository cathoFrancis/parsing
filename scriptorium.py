import os

from datetime import datetime, timedelta
import requests


def get_url():
    link = input('Укажите адрес: ').strip()
    url = link.replace('?prefix=', '')
    return url


def get_list_days():
    today = datetime.today() - timedelta(days=1)
    last_day = today - timedelta(days=681)

    start_date = today
    end_date = last_day

    dates = []

    while start_date >= end_date:
        dates.append(start_date.strftime('-%Y-%m-%d'))
        start_date -= timedelta(days=1)

    return dates


def get_coin(url, date):
    url_parts = url.split('/')
    last_part = url_parts[-3]
    time_set = url_parts[-2]

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    counter = 0  # счетчик загруженных файлов

    for i in date:
        filename = f'downloads/{last_part}-{time_set}{i}.zip'
        response = requests.get(f'{url}{filename[10:]}')

        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            counter += 1  # увеличиваем значение счетчика
        else:
            print(f'Ошибка {response.status_code}: файл не был загружен')

        print(f'Загружено {counter} файлов из {len(date)} возможных')

        if counter == len(date):
            print("Загрузка завершена !!!")



def main():
    url = get_url()
    date = get_list_days()
    get_coin(url, date)


if __name__ == '__main__':
    main()
