import pytesseract
from pytesseract import Output
import PIL.Image
import cv2

def img_to_list(image):
    myconfig = r"--psm 6 --oem 3"

    img = cv2.imread(image)

    height,width,_ = img.shape

    word_list = []

    text = pytesseract.image_to_data(img, lang="dan", config=myconfig, output_type=Output.DICT)

    amount_boxes = len(text['text'])
    for i in range(amount_boxes):
        if float(text['conf'][i]) > 70:
            word_list.append(text['text'][i])
    
    return word_list