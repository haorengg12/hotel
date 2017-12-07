from PIL import Image
import qrcode

qr=qrcode.QRCode(
    version = 5,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)
qr.add_data("认真你就输了！")

qr.make(fit = True)
img = qr.make_image()

img = img.convert("RGBA")

# icon = Image.open("A.png")

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

# icon_w, icon_h = icon.size
# if icon_w > size_w:
#     icon_w = size_w
# if icon_h > size_h:
#     icon_h = size_h
# icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)
#
# w=int((img_w - icon_w)/2)
# h=int((img_h - icon_h)/2)
#img.paste(icon, (w, h), icon )

img.save("qr.png")