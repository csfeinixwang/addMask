import qrcode
import os
import pyzbar
from pyzbar.pyzbar import decode
from PIL import Image
def decode_qr_code(code_img_path='image.jpg'):
    if not os.path.exists(code_img_path):
        raise FileExistsError(code_img_path)
    # Here, set only recognize QR Code and ignore other type of code
    return decode(Image.open(code_img_path), symbols=[pyzbar.pyzbar.ZBarSymbol.QRCODE])[0].data.decode('utf-8')

# url=decode_qr_code()
#
# print(url)