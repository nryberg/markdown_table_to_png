from html2image import Html2Image
import markdown
from PIL import Image, ImageOps

table_css = '''
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
def markdown_to_html(md):
    result = markdown.markdown(md,extensions=['tables'])
    return result

def html_to_png(html, file_name):
    hti = Html2Image(custom_flags=['--disable-features=DarkMode'])
    hti.screenshot(html_str=html, css_str=table_css, save_as=file_name)

def cropbox(file_name, output_file_name):

    img = Image.open(file_name)
    # Get the content bounds.
    content = img.getbbox(alpha_only=False)

    # Flip to RGB mode to enable invert operation.
    img_RGB=img.convert("RGB")
    invert_im = ImageOps.invert(img_RGB)

    # Get the inverted content bounds.
    inverted_content = invert_im.getbbox()

    # Crop the image.
    img = img.crop(inverted_content)

    # Save the image.
    img.save(output_file_name)

# Read markdown file
with open('table.md', 'r') as f:
    md = f.read()
    html = markdown_to_html(md) # = markdown.markdown(md,extensions=['tables'])
    html_to_png(html, 'table.png')
    cropbox('table.png', 'fixed_table.png')
#    print(md)
 #   'table.png'
