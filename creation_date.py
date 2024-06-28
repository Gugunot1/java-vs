import os
import datetime

file_path  = 'DJI_0158.JPG'

creation_date = os.path.getctime(file_path)

creation_datetime = datetime.datetime.fromtimestamp(creation_date)

print(f"Дата последнего изменения файла : {creation_datetime}")
