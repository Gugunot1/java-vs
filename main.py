
import os
from datetime import datetime
from exif import Image

with open("DJI_0206.JPG", "rb") as palm_1_file:
    palm_1_image = Image(palm_1_file)

images = [palm_1_image]

image = "DJI_0206.JPG"
for index, image in enumerate(images):
    if image.has_exif:
        status = f"contains EXIF (version {image.exif_version}) information."
    else:
        status = "does not contain any EXIF information."
    print(f"Image  {status}")
    print(f"{image.datetime_original}.")
image = "DJI_0206.JPG"
mtime = os.path.getmtime(image)
mtime_readable = datetime.fromtimestamp(mtime)
print('Modification_date:',mtime_readable)
c_timestamp = os.path.getctime(image)
c_time = datetime.fromtimestamp(c_timestamp)
print('Creation_date:',c_time)



