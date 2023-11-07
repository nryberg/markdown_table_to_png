#!/usr/bin/env python

from html2image import Html2Image
import markdown
from PIL import Image, ImageOps
import sys, getopt
import os



default_css = '''
table {
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}
thead tr {
    background-color: #3061b0;
    color: #ffffff;
    text-align: left;
}
th,
td {
    padding: 12px 15px;
}
tbody tr {
    border-bottom: 1px solid #dddddd;
}

tbody tr:nth-of-type(even) {
    background-color: #f3f3f3;
}

tbody tr:last-of-type {
    border-bottom: 2px solid #3061b0;
}
'''

def copyname(input_markdown_file):

    # Reverse the string to just get the file name
    reverse_input_markdown_file = input_markdown_file[::-1]
    reverse_file_name = reverse_input_markdown_file.split(".")[1].split("/")[0]

    # Reverse the string back to normal
    name = reverse_file_name[::-1]

    return name + ".png"

def markdown_to_html(md):
    result = markdown.markdown(md,extensions=['tables'])
    return result

def html_to_png(html, file_name, table_css):
    hti = Html2Image(custom_flags=['--disable-features=DarkMode'])
    hti.screenshot(html_str=html, css_str=table_css, save_as=file_name, size=(2500, 2580))

def cropbox(file_name, output_file_name):
    img = Image.open(file_name)

    # Flip to RGB mode to enable invert operation.
    img_RGB=img.convert("RGB")
    invert_im = ImageOps.invert(img_RGB)

    # Get the inverted content bounds.
    inverted_content = invert_im.getbbox()

    # Crop the image.
    img = img.crop(inverted_content)

    # Save the image.
    img.save(output_file_name)

def remove_temp_file():
    os.remove("temp.png")

def main(argv):
    input_markdown_file = ''
    output_png_file = ''
    table_css = default_css
    opts, args = getopt.getopt(argv,"hi:o:c:",["ifile=","ofile=", "cssfile="])
    for opt, arg in opts:
            if opt == '-h':
                print ('markdown_table_to_png.py -i <input markdown file> -o <output png file>')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                input_markdown_file = arg
                output_png_file = copyname(input_markdown_file)
            elif opt in ("-o", "--ofile"):
                output_png_file = arg
            elif opt in ("-c", "--cssfile"):
                with open(arg, 'r') as f:
                    file_css = f.read()
                    table_css = file_css

    print ('Input file is ', input_markdown_file)
    print ('Output file is ', output_png_file)

    with open(input_markdown_file, 'r') as f:
        md = f.read()
        html = markdown_to_html(md) # = markdown.markdown(md,extensions=['tables'])
        html_to_png(html, 'temp.png', table_css)
        cropbox('temp.png', output_png_file)
        remove_temp_file()

if __name__ == "__main__":
   main(sys.argv[1:])
