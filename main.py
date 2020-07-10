import pyttsx3              # Here imported the text to speech python ver3 package
import PyPDF2               # Here imported the PDF reader python ver2 package

book = open('OOP.pdf', 'rb')                    # open pdf book in the project location named meditations
pdfReader = PyPDF2.PdfFileReader(book)          # Read book variable
pages = pdfReader.numPages                      # Num of pages in this book
print('Total pages in this book is: ', pages)   # print the Total pages in this book

speaker = pyttsx3.init()                        # initialize text to speech python ver3 package

for num in range(1, pages):                     # using a for loop for reading and speaking the whole pdf file
    print('>> reading the page: ', num)         # print the current reading the page number
    page = pdfReader.getPage(num)
    text = page.extractText()                   # extracting the text from pdf file
    speaker.say(text)                           # speaking the current page of the book
    speaker.runAndWait()
