import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=5,)
qr.add_data("https://www.saritabk.com.np/")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="white")
img.save("SARITA_BK_WEBPAGE.png")