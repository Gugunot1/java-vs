
import os
from datetime import datetime
from exif import Image

filename = "1622199289.jpg"
with open(filename, "rb") as palm_1_file:
    palm_1_image = Image(palm_1_file)

palm_1_image.has_exif
dtime = os.path.getmtime(filename)
dtime_readable = datetime.fromtimestamp(dtime)
print('date_from_exif:', dtime_readable)

mtime = os.path.getmtime(filename)
mtime_readable = datetime.fromtimestamp(mtime)
print('Modification_date:',mtime_readable)
c_timestamp = os.path.getctime(filename)
c_time = datetime.fromtimestamp(c_timestamp)
print('Creation_date:',c_time)



