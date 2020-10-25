# OCR
OCR for Army Officer Evaluation Records

## Useful links
- Tutorial: https://medium.com/analytics-vidhya/optical-character-recognition-ocr-using-py-tesseract-part-1-29ba8104eb2b
- Remember to install tesseract: https://guides.library.illinois.edu/c.php?g=347520&p=4121425
- Test regex: https://regex101.com/

### How to use
- If one image with two pages (e.g. 2 pg pdf converted to .tiff)
    - Call bash extract_from_oer.sh [filename.extension] [threshold]
- If two images in two files
    - Call bash extract_from_2_pg_oer.sh [file1.extension] [file2.extension] [threshold]

### Order of executed scripts
- split_images.py
    - Split multi-page image into separate images. (good if turned pdf > image)
    - python split_images.py [img_filename]
- binarize_images.py
    - For making images more crisp
    - python binarize_images.py [theshold 0-255] [img_file1] [img_file2] [file3...]
- img_to_text.py
    - Extract text from images with tesseract + python wrapper
    - Only include images/pages from same document (page 1 and 2 of OER)
    - python img_to_text.py [oer_img_page1] [oer_img_page2]
- parse.py
    - Extract/clean raw text and ouput a json file
    - python parse.py [txt_filename]
