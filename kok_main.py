import pandas as pd
import PyPDF2
import pprint
import glob
import os
import openpyxl
pp = pprint.PrettyPrinter()



# looping through .pdf extensions only
pdf_list = []
os.chdir("updated_pdfs")
for file in glob.glob("*.pdf"):
    pdf_list.append(file)

pp.pprint(pdf_list)

#using field names as column names for dataframe
col_names = ["Job NumberRow1", "Employee Name", "Employee Number", "Total Hrs", "Total OT Hrs", "Regularhrs1", "Regularhrs2", "Regularhrs3",
    "Regularhrs4", "Regularhrs5", "Regularhrs6", "Regularhrs7", "Overtimehrs1", "Overtimehrs2", "Overtimehrs3",
    "Overtimehrs4", "Overtimehrs5", "Overtimehrs6", "Overtimehrs7", "Super1", "Super2", "Super3", "Super4", "Super5",
    "Super6", "Super7"]

df = pd.DataFrame(columns=col_names)

row_num = 0
#testing formatting
writer = pd.ExcelWriter('test_file.xlsx')


#looping through each pdf
for f in pdf_list:

  
  #opening current pdf to read
    pdf_file = open(f, 'rb')
    reader = PyPDF2.PdfFileReader(pdf_file)
    page = reader.getPage(0)

    
    row_num += 1
    fields = reader.getFields()
    print(fields['Equip  Repaired Line 1'].value)
    #inserting data from fields into dataframe
    for x in col_names:
        #df = df.astype(float)
        #df['Employee Number'] = pd.to_numeric(df['Employee Number'], downcast='float')
        
        cell_value = fields[x].value
        pp.pprint(cell_value)
        try:
            if x != 'Employee Name'and cell_value != None:
                df[x] = pd.to_numeric(df[x], downcast='float')
                df.loc[row_num, x] = cell_value
            else:
                df.loc[row_num, x] = cell_value
        except ValueError:
        
            df.loc[row_num, x] = cell_value
        #formatting column width based on length of column name
        df.to_excel(writer, sheet_name='time card', index=False, na_rep='')
        column_width = max(df[x].astype(str).map(len).max(), len(x))
        col_idx = df.columns.get_loc(x)
        writer.sheets['time card'].set_column(col_idx, col_idx, column_width)
        
pp.pprint(df)  
print('-----------------------------')     
pp.pprint(fields)
writer.save()

