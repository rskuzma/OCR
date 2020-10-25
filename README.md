# OCR
OCR for Army Officer Evaluation Records

### Useful links
- Tutorial: https://medium.com/analytics-vidhya/optical-character-recognition-ocr-using-py-tesseract-part-1-29ba8104eb2b
- Remember to install tesseract: https://guides.library.illinois.edu/c.php?g=347520&p=4121425
- Test regex: https://regex101.com/

### Required file structure
```
├── README.md          <- The top-level README for users of this project.
│
├── data
│   ├── images         <- Put your OER images here.
│   ├── text           <- Text within images is saved here.
│   └── output         <- The final, structured json is saved here
│
└── src
    ├── extract_from_oer.sh             <- Creates json from one OER image.
    ├── extract_from_2_pg_oer.sh        <- Creates json from two OER images.
    ├── split_images.py                 <- Splits one image into two.
    ├── binarize_images.py              <- Binarizes images to black and white.
    ├── img_to_text.py                  <- Converts image text to .txt file.
    └── parse.py                        <- Structures key text fields into json.
```

## How to use
- git clone this repo
- save any images of OERs into ```data/images/```
- cd into src
- If one image with two pages (e.g. 2 pg pdf converted to .tiff)
    - Format must be name.extension
    - Call ```bash extract_from_oer.sh [filename.extension] [threshold]```
- If two images in two files
    - Format must be name.page1.extension and name.page2.extension
    - Call ```bash extract_from_2_pg_oer.sh [file1.extension] [file2.extension] [threshold]```
- Threshold is required for binarization of images into black and white

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
