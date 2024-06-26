import os
import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir)

creation_date = os.path.getctime(file_path)

creation_datetime = datetime.datetime.fromtimestamp(creation_date)

print(f"Дата последнего изменения файла : {creation_datetime}")
