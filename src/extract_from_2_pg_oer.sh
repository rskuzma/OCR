#! /bin/bash
first="$1"
second="$2"
thresh="$3"
name=${first%_page*}

extension1=${first##*.}
extension2=${second##*.}

page1="_page1."
page2="_page2."
bin="_bin_"
txt=".txt"

filename_page_1=$name$page1$extension
filename_page_2=$name$page2$extension


filename_bin_page_1=$name$bin$thresh$page1$extension1
filename_bin_page_2=$name$bin$thresh$page2$extension2

txt_filename=$name$bin$thresh$txt

echo
echo "Converting OER: $first and $second, binarizing threshold: $thresh to json"
# python split_images.py $filename &&
python binarize_images.py $thresh $first $second &&
python img_to_text.py $filename_bin_page_1 $filename_bin_page_2 &&
python parse.py $txt_filename
echo
