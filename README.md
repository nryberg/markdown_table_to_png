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
| -i       | Input file  | table.md |
| -o       | Output file | table.png |


## Tasks:

- [x] Allow Command Line Arguments

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
