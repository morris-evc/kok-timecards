import pandas as pd
import PyPDF2
import pprint
import os
pp = pprint.PrettyPrinter()
pdf_file = open(r'c:\users\emorris\desktop\git\kok-timecards\timecard_pdfs\6 26 21 Time Card.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdf_file)
page = reader.getPage(0)
#print(page.extractText())
field_data_list = []
col_names = ["Employee Name", "Employee Number", "Total Hrs", "Total OT Hrs", "Regularhrs1", "Regularhrs2", "Regularhrs3",
"Regularhrs4", "Regularhrs5", "Regularhrs6", "Regularhrs7"]

df = pd.DataFrame(columns=col_names)


page_fields_list = [page.extractText()]
#pp.pprint(page_fields_list)
#field_data_list = [reader.getFields()]
fields = reader.getFields()


for x in col_names:
    df.loc[1, x] = fields[x].value
    #print(fields[x].value)
print(df)

#pp.pprint(field_data_list)
#print(field_data_list.count)

#for item in field_data_list:
  # pp.pprint(item)