from html2image import Html2Image
import markdown
from PIL import Image, ImageOps
import sys, getopt

def markdown_to_html(md):
    result = markdown.markdown(md,extensions=['tables'])
    return result

def html_to_png(html, file_name):
    hti = Html2Image(custom_flags=['--disable-features=DarkMode'])
    hti.screenshot(html_str=html, css_str=table_css, save_as=file_name)

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

# Read in the CSS File
with open('table.css', 'r') as f:
    table_css = f.read()


# Read markdown file

with open('table.md', 'r') as f:
    md = f.read()
    html = markdown_to_html(md) # = markdown.markdown(md,extensions=['tables'])
    html_to_png(html, 'table.png')
    cropbox('table.png', 'fixed_table.png')
