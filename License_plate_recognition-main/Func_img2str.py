import pytesseract
import cv2
from Func_mask_to_rect import mask_to_rect

def Img2Str(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.bilateralFilter(gray, 10, 15, 15)

    cf = '--oem 3 --psm 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    text = pytesseract.image_to_string(img_blur, lang='eng', config=cf)
    if (len(text) > 0):
        return text
    else:
        img_max = mask_to_rect(gray)
        img_blur = cv2.bilateralFilter(gray, 10, 15, 15)
        text = pytesseract.image_to_string(img_blur, lang='eng', config=cf)
        return text