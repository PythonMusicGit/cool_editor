from PIL import Image
from PIL import ImageFilter
# для бонусного завдання
from PIL import ImageEnhance
import os
Folder = 'C:\\Users\\admin\\Desktop\\project\\images'
i = 0

for imagefile in os.listdir(Folder):
    image_path = os.path.join(Folder, imagefile)
    i += 1
    with Image.open(image_path) as pic_original:
        pass
        pic_original.show()
        pic_original.save(f'original{i}.jpg')
        pic_gray = pic_original.convert('L')
        pic_gray.save(f'gray{i}.jpg')
        pic_gray.show()
        pic_blured = pic_original.filter(ImageFilter.BLUR)
        pic_blured.save(f'blur{i}.jpg')
        pic_blured.show()
        pic_up = pic_original.transpose(Image.ROTATE_180)
        pic_up.save(f'up{i}.jpg')
        pic_up.show()
        pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
        pic_mirrow.save(f'mirrow{i}.jpg')
        pic_mirrow.show()
        pic_contrast = ImageEnhance.Contrast(pic_original)
        pic_contrast = pic_contrast.enhance(1.5)
        pic_contrast.save(f'contrast{i}.jpg')
        pic_contrast.show()