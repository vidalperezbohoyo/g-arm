import os
import PyPDF2

def remove_first_page(pdf_path):
    with open(pdf_path, 'rb') as original_file:
        pdf_reader = PyPDF2.PdfReader(original_file)
        
        pdf_writer = PyPDF2.PdfWriter()
        
        # Skip this pdf
        if len(pdf_reader.pages) == 1:
            return

        for page_num in range(1, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
        
        with open(f"without_first_page_{os.path.basename(pdf_path)}", 'wb') as new_pdf:
            pdf_writer.write(new_pdf)

# Path to the directory containing the PDF files
pdf_directory = "."

# Iterate over all files in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        file_path = os.path.join(pdf_directory, filename)
        remove_first_page(file_path)

print("Process completed.")
