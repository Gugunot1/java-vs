
import os
from datetime import datetime
from exif import Image

filename = "1622199289.jpg"
with open(filename, "rb") as palm_1_file:
    palm_1_image = Image(palm_1_file)

if palm_1_image.has_exif:
    status = f"contains EXIF (version {palm_1_image.exif_version}) information."
else:
    status = "does not contain any EXIF information."
print(f"Image {filename} {status}")
mtime = os.path.getmtime(filename)
print('Exif data:',mtime)
mtime_readable = datetime.fromtimestamp(mtime)
print('Modification:',mtime_readable)
c_timestamp = os.path.getctime(filename)
print('Creation:',c_timestamp)


