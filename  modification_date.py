import os
import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))

filename = input("Введите имя файла: ")

file_path = os.path.join(current_dir, filename)

modification_date = os.path.getmtime(file_path)

modification_datetime = datetime.datetime.fromtimestamp(modification_date)

print(f"Дата последнего изменения файла {filename}: {modification_datetime}")