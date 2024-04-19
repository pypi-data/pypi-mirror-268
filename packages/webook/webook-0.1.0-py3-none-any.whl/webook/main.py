import os
import tempfile
from PyPDF2 import PdfWriter
import requests
from PIL import Image
from webook import web
from webook.cli import options
from webook.urls import parse

def make_cover(cover: str, tempdir: str) -> str:
    """
    Conver an image to a pdf page

    Parameters:
    -----------
    cover: str
        The path or URL to the image file
    tempdir: str
       The path to the temporary directory

    Returns:
    --------
    str
        The path to the PDF file
    """

    if os.path.exists(cover):
        img = Image.open(cover)
    else:
        img = Image.open(requests.get(cover, stream=True).raw)
    blank_image = Image.new('RGB', (595, 842), 'white')
    img = img.resize((595, int(595 * img.height / img.width)))
    blank_image.paste(img, ((595 - img.width) // 2, (842 - img.height) // 2))
    pdf = f"{tempdir}/Cover.pdf"
    blank_image.save(pdf, "PDF", resolution=72.0, save_all=True)
    return pdf

def merge(pdfs: list[str], output_file: str):
    merger = PdfWriter()

    for filename in pdfs:
        input_pdf = open(filename, 'rb')
        outline_name = os.path.basename(filename)
        outline_name = os.path.splitext(outline_name)[0]
        merger.append(input_pdf, outline_item=outline_name)

    output_pdf = open(output_file, 'wb')
    merger.write(output_pdf)
    merger.close()
    output_pdf.close()


def main():
    with tempfile.TemporaryDirectory() as tempdir:
        pdfs = []
        if options.cover:
            pdfs.append(make_cover(options.cover, tempdir))
        pdfs.extend(web.save_as_pdf(parse(options.url_file), tempdir, options))
        merge(pdfs, options.output_file)


if __name__ == "__main__":
    main()