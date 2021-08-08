#you have to install PyPDF2 to listen a pdf reading by your virtual friend
#need a pdf file which must remain in the same folder where this 2.py file.

import pyttsx3
friend = pyttsx3.init()
friend.say('Permit me to talk,please!')
friend.runAndWait()