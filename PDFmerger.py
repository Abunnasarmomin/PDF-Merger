import PyPDF2

en = input("Enter The pdf name you want to merge: ")#.split(".pdf")
en1 = input("Enter The Merged Pdf Name: ")#.split('.pdf')

pdfFiles = en.split() 
merger = PyPDF2.PdfMerger()

for filename in pdfFiles:
   with open(filename, "rb") as PdfFile:
        PdfReader = PyPDF2.PdfReader(PdfFile)
        merger.append(PdfReader)

with open(en1, "wb") as mergedPdf:
    merger.write(mergedPdf)

print(f"Merged PDF saved as: {en1}")

