import os
from datetime import datetime

current_file = os.path.realpath(__file__)

creation_date = os.path.getctime(current_file)

creation_date_str = datetime.fromtimestamp(creation_date).strftime('%Y-%m-%d %H:%M:%S')

print(f'Дата создания файла: {creation_date_str}')