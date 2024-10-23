import PyPDF2

file_path = "C:/Users/sriva/Desktop/TTD/TimeTable-Division/TT CHANGES - 5.pdf"

with open(file_path,'rb') as file:
    reader = PyPDF2.PdfReader(file)

    pdf_text = ""

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]

        pdf_text+=page.extract_text()

        print(pdf_text)