# Markdown Table to PNG converter

Useful for converting Markdown tables to PNGs for later import.

## Requirements

- [Headless](https://developer.chrome.com/blog/headless-chrome/) Chrome to function.
- [Pillow](https://python-pillow.org/) for image manipulation.
- [html2Image](https://github.com/vgalin/html2image) for image generation.
- [Markdown](https://python-markdown.github.io/) for Markdown parsing.

## Example Table

```markdown
| fruit  | price  |
|--------|--------|
| apple  | 2.05   |
| pear   | 1.37   |
| orange | 3.09   |
```

Results:

![Example Table](fixed_table.png)

## Usage

```shell
python ./markdown_table_to_png.py -i table.md -o table.png
```

### Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-i`       | Input file  | table.md |
| `-o`       | Output file | table.png |
| `-c`    | CSS File  | table.css |


## CSS

CSS is built in with a default value so you can run this script anywhere.  However, if you want to override it - say pick different colors, you can do so by passing in a CSS file.

```shell
python ./markdown_table_to_png.py -i table.md -o table.png -c my_table.css
```

*Example CSS File*

```css
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
```

## Tasks:

- [x] Allow Command Line Arguments
- [x] Allow CSS file to be passed in

- [ ] Figure out the column width question - is it controlled by the page?
- [ ] Add support for more table styles.
- [ ] Add support for more Markdown styles.
- [ ] Add support for more image formats. (Currently only PNG)
- [ ] Add support for more image manipulation. (Currently only resizing)
- [ ] Allow for multiple tables in one image.
- [ ] Datestamp the output image name if there are multiple
- [ ] Allow different colors for the table.
- [ ] Build out the table.css file to allow for more customization.
- [ ] Add a header for the table
- [ ] Add a footer for the table
