from PIL import Image
from PIL import ImageFilter


class :
    def __init__(self):
        pass


    def open(self):
        pass


    def do_left(self):
        pass


    # бонус. Обрізати фотографію
    def do_cropped(self):
        pass


MyImage = ImageEditor('original_new.jpg')
MyImage.open()


MyImage.do_left()
MyImage.do_cropped()


for im in MyImage.changed:
    im.show()
