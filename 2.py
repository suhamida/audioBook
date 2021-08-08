#you have to install PyPDF2 to listen a pdf reading by your virtual friend
#need a pdf file which must remain in the same folder where this 2.py file.

import pyttsx3
import PyPDF2
book = open('The Alchemist.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()
page = pdfReader.getPage(7) #for specific page
text = page.extractText()
friend.say(text)
friend.runAndWait()