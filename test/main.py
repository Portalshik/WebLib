import pypdfium2 as pdfium


def pdf2jpg(filepath):
    pdf = pdfium.PdfDocument(filepath)

    # render a single page (in this case: the first one)
    page = pdf.get_page(0)
    pil_image = page.render_to(
        pdfium.BitmapConv.pil_image,
    )

    pil_image.save(f"static/imgs/{filepath.split('/')[-1].replace('.pdf', '')}.jpg")
