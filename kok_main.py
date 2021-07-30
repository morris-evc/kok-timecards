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

#using field names as colimn names for dataframe
col_names = ["Employee Name", "Employee Number", "Total Hrs", "Total OT Hrs", "Regularhrs1", "Regularhrs2", "Regularhrs3",
    "Regularhrs4", "Regularhrs5", "Regularhrs6", "Regularhrs7", "Overtimehrs1", "Overtimehrs2", "Overtimehrs3",
    "Overtimehrs4", "Overtimehrs5", "Overtimehrs6", "Overtimehrs7", "Super1", "Super2", "Super3", "Super4", "Super5",
    "Super6", "Super7"]

df = pd.DataFrame(columns=col_names)

row_num = 0

#looping through each pdf
for f in pdf_list:

  
  #opening current pdf to read
    pdf_file = open(f, 'rb')
    reader = PyPDF2.PdfFileReader(pdf_file)
    page = reader.getPage(0)

    
    row_num += 1
    fields = reader.getFields()
   
    #inserting data from fields into dataframe
    for x in col_names:
        
        df.loc[row_num, x] = fields[x].value
    
    
#creating .csv
df.to_csv('test.csv')
