from PyPDF2 import PdfReader
def get_pdf_text(pad_doc):
    text = ""
    for page in pad_doc:
        no_pages =  PdfReader(page)
        for page in no_pages.pages:
            text += page.extract_text()    
    return text
