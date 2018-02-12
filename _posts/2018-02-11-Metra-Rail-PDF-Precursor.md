### Metra Rail Data: PDF Precursor

Occasionally I have the distinct displeasure of working with data locked away in PDFs. Last week I was thinking about the Metra commuter rail system in the Chicago metropolitan area, and found their data page. Of course, these reports were in everyone's favorite format, tables embedded into PDF files. After a bit of googling and attempting a few different things I happened upon a reliable way to pull out the information I wanted. Before I actually do anything with that data I thought it might be useful to write up that process, and just how I think about PDF files in general.

# 4 Rules
1. It's relatively easy to get raw text from a modern pdf.
2. Rule 1 does not apply to scanned or handwritten docs.
3. Beyond raw text, java (or java bindings) is probably involved. 
4. You're still going to need to manually QA/QC formatting.

# The Process

So how to get the PDF into Python to begin with? I'll often turn to PyPDF2. [PyPDF2 is an excellent pure-python library](https://github.com/mstamy2/PyPDF2) for extracting pdf text, as well as copying/saving/slicing pdf files together. In this case, you could pull in the tables as pure text in all of their character formatting glory, but it seems easier to me to end up with a dataframe and work from there. To do that we'll use tabula-py, [which is a library that provides python bindings](https://github.com/chezou/tabula-py) for tabula-java. Since it's based on a java app you'll also need to install java and make sure it's in your PATH (if you're on Windows). 

First I attempted to just feed tabula the entire pdf via the read_pdf() function. This didn't work (although I didn't really expect it to), so I tried to use one of the optional commands and feed it a specific page.  Surprisingly, 

```
read_pdf("data.pdf", pages=3)
```

also didn't work. At this point I knew something was up, but the error message wasn't clear to me and I wasn't about to debug a some java bindings for fun. This seems to happen every time I try to pull data from a PDF (because it's a format that was never really intended to be used in this way), something goes wrong, I'm not sure why, and try slightly different things until one works.
This time around, the first  thing I tried resulted in success. I knew I could slice apart a PDF with PyPDF2, and save the desired page object individually as a new pdf, so my plan of attack was to pull out a page I knew was a table, save it as a new pdf, and feed it to tabula as a 1 pager that  was certain only contained a table.  

![The messy starting table.](https://farm5.staticflickr.com/4712/39315052655_e1807f35f5_z.jpg)

In this case I think the simplest way to get to my desired result is individual construction of the lists that will comprice the columns in the dataframe. 

```
from tabula import read_pdf
import PyPDF2

pdfFileObj = open('trains16.pdf', 'rb')

pdfWriter = PyPDF2.PdfFileWriter()
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(6)
pdfWriter.addPage(pageObj)

resultPdf = open('testsave.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()

```
![Success!](https://farm5.staticflickr.com/4632/28433439879_96b0445780_z.jpg)


In this case, the data has split column headers, multiple data points in individual "cells", and mixed string/integer data. This is where rule comes into the picture. You've got a nice dataframe in that everything is there and in roughly the right place, but it's still a bit muddled, and not in the row/column ordering I intuitively want. I'll typically write out a data structure with paper/whiteboard. Otherwise, I tend to waste a lot of time idly looping through the data and trying to organize it on the fly.

![Rough translation.](https://farm5.staticflickr.com/4764/25342486717_347ef396fc_z.jpg)
