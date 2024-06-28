import os
import datetime

file_path = "DJI_0157.JPG"

modification_date = os.path.getmtime(file_path)

modification_datetime = datetime.datetime.fromtimestamp(modification_date)

print(f"Дата последнего изменения файла : {modification_datetime}")