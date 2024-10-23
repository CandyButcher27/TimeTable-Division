import pdfplumber
import json

file_path = "C:/Users/sriva/Desktop/TTD/TimeTable-Division/TT CHANGES - 5.pdf"
json_file_path = "extracted_Data.json"

table_data = []

with pdfplumber.open(file_path) as pdf :

    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        tables = page.extract_tables()

        for table in tables : 
            if(page_num==0):
                headers = table[0]
            for row in table[1:]:
               row_data = {headers[i]:row[i]  for i in range(len(headers))}
               table_data.append(row_data)

with open(json_file_path,'w') as json_file :
    json.dump(table_data,json_file,indent=4)

print(f"The data has been saved into the {json_file_path} in a proper format")
    

        
        
    
