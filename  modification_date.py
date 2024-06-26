import os
import datetime

current_file_path = os.path.abspath(__file__)

directory = os.path.dirname(current_file_path)

file_path = os.path.join(directory)

modification_date = os.path.getmtime(file_path)

modification_datetime = datetime.datetime.fromtimestamp(modification_date)

print(f"Дата последнего изменения файла {file_path}: {modification_datetime}")