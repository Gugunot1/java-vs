import os
import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir)

modification_date = os.path.getmtime(file_path)

modification_datetime = datetime.datetime.fromtimestamp(modification_date)

print(f"Дата последнего изменения файла : {modification_datetime}")