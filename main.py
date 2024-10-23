import pdfplumber
import json

file_path = "C:/Users/sriva/Desktop/TTD/TimeTable-Division/TT CHANGES - 5.pdf"
json_file_path = "extracted_Data.json"

table_data = []

#Extracting the data
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

#Putting the data in a json file 
with open(json_file_path,'w') as json_file :
    json.dump(table_data,json_file,indent=4)

#Cleaning the data
with open(json_file_path,'r') as file:
    data = json.load(file)

    previous_values={}

    for entry in data :
        
        for key,value in entry.items():
            if value=="":
                entry[key] = previous_values.get(key,"")
            else :
                previous_values[key] = value
        
        if 'SlNo' in entry :
            entry['SlNo'] = entry['SlNo'].replace(')','')
        
        if 'Course Title' in entry :
            entry['Course Title'] = entry['Course Title'].replace('\n','')
        
        if 'New' in entry :
            entry['New'] = entry['New'].replace('\n','')
        
        if 'Existing' in entry:
            entry['Existing'] = entry['Existing'].replace('\n','')


with open(json_file_path,'w') as file:
    json.dump(data,file,indent=4)

print("Json has been formatted")
    
    

        
        
    
