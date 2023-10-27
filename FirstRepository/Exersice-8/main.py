from PyPDF2 import PdfReader

reader = PdfReader("Exercise-8/dummy.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()