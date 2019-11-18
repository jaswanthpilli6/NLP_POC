import PyPDF2

pdf_file = open('AR_2017.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()

print(number_of_pages)

text = ''
for i in range(number_of_pages):
    page_content = read_pdf.getPage(i).extractText()
    print(page_content)
    text = text + ' '.join(page_content.split()) + ' '
    print('------------------------------------------')


# print(text)
