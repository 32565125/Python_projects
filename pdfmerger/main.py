import PyPDF2

pdfiles = ["Chapter 10 - Oops.pdf" , "MSC Bioinformatics Elphinstone College.pdf" , "Python_Complete_Notes.pdf" ]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFiles = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFiles)
    merger.append(pdfReader)
pdfFiles.close()
merger.write('merged.pdf')





