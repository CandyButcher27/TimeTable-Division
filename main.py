import pdfplumber

file_path = "C:/Users/sriva/Desktop/TTD/TimeTable-Division/TT CHANGES - 5.pdf"

table_data = []

with pdfplumber.open(file_path) as pdf :

    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        tables = page.extract_tables()

        for table in tables : 
            if(page_num==0):
                headers = table[0]
            for row in table[1:]:
               for i in range(len(headers)):
                   row_data = {headers[i]:row[i]}
                   table_data.append(row_data)

    print(table_data)
    

        
        
    
