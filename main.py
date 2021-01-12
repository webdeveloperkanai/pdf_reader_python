import pyttsx3
import PyPDF2
name = input("Enter pdf name and it should be in same dir : ")
no = int(input("Enter starting page : "))
book = open(name,'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
sp = pyttsx3.init()
for num in range (no,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)
    sp.say(text)
    sp.runAndWait()
