import json
from tkinter import *
from tkinter.ttk import Combobox
import subprocess


def save_car_and_commit():
    brand = combo_brand.get()
    model = combo_model.get()
    year = entry_year.get()
    color = entry_color.get()
    number_plate = entry_number.get()
    owner = entry_owner.get()

    if not all([brand, model, year, color, number_plate, owner]):
        label_status.config(text='Заполните все поля!', fg='red')
        return

    try:
        with open('cars.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    new_car = {'brand': brand, 'model': model, 'year': int(year),
               'color': color, 'numberPlate': number_plate,
               'owner': owner}

    data.append(new_car)

    with open('cars.json', 'w') as file:
        json.dump(data, file, indent=4)

    # Добавляем изменение в индекс Git
    subprocess.run(['git', 'add', 'cars.json'])

    # Коммитим изменения
    message = f"Added a new car: {brand} {model}"
    subprocess.run(['git', 'commit', '-m', message])

    # Пушим изменения в удаленный репозиторий
    subprocess.run(['git', 'push'])

    label_status.config(text=f'Автомобиль {brand} {model}, {year}-го года успешно сохранён и отправлен в репозиторий.', fg='green')


if __name__ == '__main__':
    root = Tk()
    root.title("Добавление нового автомобиля")
    root.geometry("400x300")

    brands = ['Toyota', 'Ford', 'BMW']
    models = ['Camry', 'Mustang', 'X5']

    Label(root, text="Марка:").grid(row=0, column=0, sticky=E)
    combo_brand = Combobox(root, values=brands)
    combo_brand.grid(row=0, column=1)

    Label(root, text="Модель:").grid(row=1, column=0, sticky=E)
    combo_model = Combobox(root, values=models)
    combo_model.grid(row=1, column=1)

    Label(root, text="Год выпуска:").grid(row=2, column=0, sticky=E)
    entry_year = Entry(root)
    entry_year.grid(row=2, column=1)

    Label(root, text="Цвет:").grid(row=3, column=0, sticky=E)
    entry_color = Entry(root)
    entry_color.grid(row=3, column=1)

    Label(root, text="Номерной знак:").grid(row=4, column=0, sticky=E)
    entry_number = Entry(root)
    entry_number.grid(row=4, column=1)

    Label(root, text="Владелец:").grid(row=5, column=0, sticky=E)
    entry_owner = Entry(root)
    entry_owner.grid(row=5, column=1)

    Button(root, text="Сохранить автомобиль", command=save_car_and_commit).grid(row=6, columnspan=2, pady=10)

    label_status = Label(root, text="", fg="black")
    label_status.grid(row=7, columnspan=2)

    root.mainloop()