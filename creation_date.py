import os
import datetime

current_file_path = os.path.abspath(__file__)

directory = os.path.dirname(current_file_path)

file_path = os.path.join(directory)

creation_date = os.path.getctime(file_path)

creation_datetime = datetime.datetime.fromtimestamp(creation_date)

print(f"Дата последнего изменения файла {file_path}: {creation_datetime}")

