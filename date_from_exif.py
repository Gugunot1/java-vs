import exif 
from exif import Image

def date_from_exif(file_name):
    try:
        with open(file_name, 'rb') as f:
            image = exif.Image(f)
            if 'EXIF' in image.tags:
                exif_data = image.has_exif
                if 'DateTime' in exif_data:
                    date_time = exif_data['DateTime']
                    if date_time is not None:
                        print(date_time)
                    else:
                        print('null')
                else:
                    print('null')
            else:
                print('null')
    except Exception as e:
     print(e)
if __name__ == '__main__':
    file_name = 'DJI_0160.JPG'
    date_from_exif(file_name)