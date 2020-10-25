# Richard Kuzma, October 2020
# tutorial: https://medium.com/analytics-vidhya/optical-character-recognition-ocr-using-py-tesseract-part-1-29ba8104eb2b
# kylo_ren OERs are .png and others are .tiff

# note on jupyter notebook env troubles
# python -m ipykernel install --user --name ENVNAM --display-name "WHAT DISPLAYS IN JUPYTER NOTEBOOK KERNEL SELECTION"

import os, sys
sys.path.append('/usr/local/Cellar/tesseract/4.1.1/bin/')
# # tesseract must be in your PATH or include this line with path to tesseract
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from PIL import Image, ImageSequence


def binarize(image_to_transform, threshold):
    # convert to grayscale
    output_image=image_to_transform.convert("L")
    for x in range(output_image.width):
        for y in range(output_image.height):
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x,y))< threshold: #note that the first parameter is actually a tuple object
                output_image.putpixel( (x,y), 0 )
            else:
                output_image.putpixel( (x,y), 255 )
    return output_image

def resize(img, basewidth = 675):
    print('original width, height: {}'.format(img.size))
    wpercent = (basewidth / float(img.size[0]))
    print('resizing using basewidth {}. {}%'.format(basewidth, wpercent*100))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    print('resized width, height: {}'.format(img.size))
    return img



### main
def main():
    thresh = 200
    # load image
    if len(sys.argv) < 3:
        sys.exit('binarize_images.py [threshold] [filename] [filename] ...')
        # pass


    if not sys.argv[1].isdigit():
        print('binarize_images.py [threshold] [filename] [filename] ...')
        sys.exit('Threshold must be a integer')
    elif (int(sys.argv[1]) > 0) & (int(sys.argv[1]) < 256):
        thresh = int(sys.argv[1])
    else:
        print('Threshold must be between 0 and 255 inclusive')
        print('Defaulting to 200...')
        pass


    args = sys.argv[2:]
    IMG_PATH = '../data/images/'
    OUTPUT_PATH = '../data/outputs/'
    for arg in args:
        print('\n')
        img_filename= arg
        img_name = img_filename[0:img_filename.index('page')-1]
        img_page = img_filename[img_filename.index('page'):img_filename.rindex('.')]
        img_ext = img_filename[img_filename.rindex('.'):]
        img = Image.open(IMG_PATH + img_filename)

        print('reading: ' + img_filename)
        print('from: ' + IMG_PATH)
        print('name: ' + img_name)
        print('page: ' + img_page)
        print('ext: ' + img_ext)
        print("Binarizing... Thresh = " + str(thresh))


        bin = binarize(img, thresh)
        bin.save(IMG_PATH + img_name + '_bin_' + str(thresh) + '_' + img_page + img_ext)
        print('img binarized.')


if __name__ == "__main__" :
    main()
