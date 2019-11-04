
from PIL import Image
from PIL.ExifTags import TAGS
import datetime, os

def get_exif_made_date(fn):    
    m_date  =   None
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        if decoded  ==   "DateTimeDigitized":
            m_date  =   datetime.datetime.strptime(value[0:10], "%Y:%m:%d")
            break

    # if m_date   ==  None:
    #     os.ge

    return m_date


# C:\python\Djaday\image_meta.py C:\python\unnamed.jpg
file    =   "C:/python/IMG_5583.jpg"
# file    =   "C:/python/unnamed.jpg"

m=    get_exif_made_date(file)
print("Date create: ",m)

