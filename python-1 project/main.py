import pyttsx3
import PyPDF2

book = open('book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

for num in range(8, pages):
    speaker = pyttsx3.init()
    page = pdfReader.getPage(8)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
