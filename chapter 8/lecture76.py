"""All abiut the pyPDF"""
# Write a program to manipulate pdf files using pyPDF. 
# Your programs should be able to merge multiple pdf files into a single pdf. 
# You are welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. 
# It can also add custom data, viewing options, and passwords to PDF files. 
# pypdf can retrieve text and metadata from PDFs as well.
from pypdf import PdfWriter, PdfReader
import os

folder_path = "pdf"
pdf_files = sorted(os.listdir(folder_path))  # Optional: sort files alphabetically

writer = PdfWriter()

for pdf_file in pdf_files:
    if pdf_file.lower().endswith(".pdf"):
        full_path = os.path.join(folder_path, pdf_file)
        reader = PdfReader(full_path)
        for page in reader.pages:
            writer.add_page(page)

# Save the merged PDF
with open("merged_output.pdf", "wb") as output_file:
    writer.write(output_file)
