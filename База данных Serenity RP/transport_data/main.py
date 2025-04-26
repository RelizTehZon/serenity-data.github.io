from flask import Flask, render_template
import pandas as pd
import requests

app = Flask(__name__)

# Репозиторий и путь к файлу CSV
REPO_URL = 'https://github.com/RelizTehZon/transport_data/blob/main/cars.csv'


@app.route('/')
def index():
    # Загружаем файл CSV из репозитория GitHub
    response = requests.get(REPO_URL)

    if response.status_code != 200:
        return f'Ошибка загрузки данных! Код статуса {response.status_code}'

    # Преобразование CSV-данных в DataFrame
    df = pd.read_csv(response.text.splitlines())

    # Конвертируем данные в словарь, чтобы передать шаблону
    cars_list = df.to_dict('records')

    return render_template('index.html', cars=cars_list)


if __name__ == '__main__':
    app.run(debug=True)