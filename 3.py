
import pyttsx3
import PyPDF2
book = open('The Alchemist.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()

for num in range(2, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()
