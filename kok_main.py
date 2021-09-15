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
col_names = ["Employee Number", "Today Date", "jcco", "Job NumberRow", "CostPhase CodeRow", "Employee Name", "Class Line ", "Regularhrs", "Overtimehrs", "Equip Repaired ", "Super", "earn"]
has_rows = ["jcco", "Job NumberRow", "CostPhase CodeRow", "Regularhrs", "Overtimehrs", "Class Line ", "Equip Repaired ", "Super", "earn"]
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
    #pp.pprint(fields)
    #print(fields['Equip  Repaired Line 1'].value)
    #inserting data from fields into dataframe
    count = 1


    while count < 8:
        for x in col_names:

        
            cell_value = ''
            if x in has_rows:  

                spec = f'{x}{count}'                      
                #print(spec)
                #print(fields[spec].value)
                cell_value = fields[spec].value

                print("run")
                if x == 'earn' and cell_value == '---':
                    print('running')
                    if fields[f'Overtimehrs{count}'].value != None:
                        cell_value = 2
                    else:
                        cell_value = 1


            else:
                cell_value = fields[x].value
            #pp.pprint(cell_value)
            try:
                if x != 'Employee Name'and cell_value != None:
                    df[x] = pd.to_numeric(df[x], downcast='float')
                    df.loc[count, x] = cell_value
                else:
                    df.loc[count, x] = cell_value
            except ValueError:
            
                df.loc[count, x] = cell_value
            #formatting column width based on length of column name
            df.to_excel(writer, sheet_name='time card', index=False, na_rep='')
            column_width = max(df[x].astype(str).map(len).max(), len(x))
            col_idx = df.columns.get_loc(x)
            writer.sheets['time card'].set_column(col_idx, col_idx, column_width)
            
        count += 1

writer.save()

