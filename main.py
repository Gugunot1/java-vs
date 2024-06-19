
import os
from datetime import datetime
from exif import Image

filename = "1622199289.jpg"
with open(filename, "rb") as palm_1_file:
    palm_1_image = Image(palm_1_file)

mtime = os.path.getmtime(filename)
if palm_1_image.has_exif:
    status = f"contains EXIF (version {palm_1_image.exif_version}) information."
    mtime = os.path.getmtime(filename)
    print('date_from_exif:', mtime)
else:
    status = "does not contain any EXIF information."
print(f"Image {filename} {status}")
mtime_readable = datetime.fromtimestamp(mtime)
print('Modification_date:',mtime_readable)
c_timestamp = os.path.getctime(filename)
c_time = datetime.fromtimestamp(c_timestamp)
print('Creation_date:',c_time)



