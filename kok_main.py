import pandas as pd
import PyPDF2
import pprint
import glob
import os
pp = pprint.PrettyPrinter()


# looping through .pdf extensions only
pdf_list = []
os.chdir("timecard_pdfs")
for file in glob.glob("*.pdf"):
    pdf_list.append(file)

pp.pprint(pdf_list)

col_names = ["Employee Name", "Employee Number", "Total Hrs", "Total OT Hrs", "Regularhrs1", "Regularhrs2", "Regularhrs3",
    "Regularhrs4", "Regularhrs5", "Regularhrs6", "Regularhrs7", "Overtimehrs1", "Overtimehrs2", "Overtimehrs3",
    "Overtimehrs4", "Overtimehrs5", "Overtimehrs6", "Overtimehrs7", "Super1", "Super2", "Super3", "Super4", "Super5",
    "Super6", "Super7"]

df = pd.DataFrame(columns=col_names)

row_num = 0

for f in pdf_list:

    #pdf_file = open(r'c:\users\emorris\desktop\git\kok-timecards\timecard_pdfs\6 26 21 Time Card.pdf', 'rb')
    pdf_file = open(f, 'rb')
    reader = PyPDF2.PdfFileReader(pdf_file)
    page = reader.getPage(0)
    #print(page.extractText())
    field_data_list = []
    
    row_num += 1

    page_fields_list = [page.extractText()]
    #pp.pprint(page_fields_list)
    #field_data_list = [reader.getFields()]
    fields = reader.getFields()
   

    for x in col_names:
        
        df.loc[row_num, x] = fields[x].value
        #print(fields[x].value)
    
print(df)
df.to_csv('test.csv')
#testing csv
#df.to_csv('test.csv')
#pp.pprint(field_data_list)
#print(field_data_list.count)

#for item in field_data_list:
  # pp.pprint(item)