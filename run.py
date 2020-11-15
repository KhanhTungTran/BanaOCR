import os
import pytesseract
import cv2
from skimage import io
import numpy as np

inputsDir = 'inputs'
outputsDir = 'outputs'
imageName = list(filter(lambda file: file[-3:] == 'png', os.listdir(inputsDir)))

def loadImage(img_file):
    img = io.imread(img_file)           # RGB order
    if img.shape[0] == 2: img = img[0]
    if len(img.shape) == 2 : img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    if img.shape[2] == 4:   img = img[:,:,:3]
    img = np.array(img[:,:,::-1])

    return img

for image in imageName:
    img = io.imread(inputsDir + '/' + image)
    print(img.shape)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = loadImage(inputsDir + '/' + image)
    cv2.imshow("original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    custom_oem_psm_config = '--psm 6'

    with open(outputsDir + '/' + image[:-3] + 'txt', 'w', encoding='utf-8') as f:
        f.write(pytesseract.image_to_string(img, lang='vie', config=custom_oem_psm_config))