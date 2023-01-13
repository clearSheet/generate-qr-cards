from PIL import Image
#
# im2 = Image.open('qr_code_109246.jpg')
# im1 = Image.open('fon.jpg')
#
# im2 = im2.resize((450, 450))
#
# back_im = im1.copy()
# back_im.paste(im2, (275, 265))
# back_im.save('fon_pillow_paste.jpg', quality=100)
#
# im1.close()
# im2.close()
#
import os

dir = 'qr'

test = os.listdir(dir)

for item in test:
    im2 = Image.open(f'qr/{item}')
    im1 = Image.open('fon.jpg')

    im2 = im2.resize((450, 450))

    back_im = im1.copy()
    back_im.paste(im2, (275, 265))
    back_im.save(f'new/{item}', quality=100)

    im1.close()
    im2.close()