import pandas as pd
import PyPDF2
import os

pdf_file = open(r'c:\users\emorris\desktop\git\kok-timecards\timecard_pdfs\6 26 21 Time Card.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdf_file)
page = reader.getPage(0)

field_data = reader.getFields()
#print(field_data)

fd_series = pd.Series(field_data)
#print(fd_series)

print(field_data['Employee Name'].value)