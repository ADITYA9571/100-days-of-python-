# Write a program to manipulate pdf files using pyPDF.
# Your programs should be able to merge multiple pdf files into a single pdf.
# You are welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and
#  transforming the pages of PDF files.
# It can also add custom data, viewing options, and passwords to PDF files.
# pypdf can retrieve text and metadata from PDFs as well.
# import os

# 1️⃣ MERGE MULTIPLE PDFs
from pypdf import PdfWriter, PdfReader

def merge_pdfs(pdf_list, output_filename):
    writer = PdfWriter()

    for pdf_path in pdf_list:
        writer.append(pdf_path)  # Add each PDF to the end
        print(f"Appended: {pdf_path}")

    writer.write(output_filename)  # Write the combined PDF
    print(f"Saved merged PDF as: {output_filename}")

# Usage
if __name__ == "__main__":
    pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
    merge_pdfs(pdf_files, "merged_output.pdf")

# 2️⃣ SPLIT PDF INTO INDIVIDUAL PAGES
def split_pdf(input_pdf):
    reader = PdfReader(input_pdf)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_filename = f"page_{i+1}.pdf"
        with open(output_filename, "wb") as f:
            writer.write(f)
        print(f"[SPLIT] Saved: {output_filename}")
    print()

# 3️⃣ EXTRACT TEXT FROM A PDF
def extract_text(input_pdf):
    reader = PdfReader(input_pdf)
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"[TEXT] Page {i+1}:\n{text}\n{'-'*50}")

# 4️⃣ ROTATE A PAGE
def rotate_page(input_pdf, page_number, degrees, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i == page_number - 1:  # 1-based page number
            page.rotate(degrees)
            print(f"[ROTATE] Rotated page {page_number} by {degrees} degrees.")
        writer.add_page(page)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"[ROTATE] Saved rotated PDF as: {output_pdf}\n")

# 5️⃣ ADD METADATA TO A PDF
def add_metadata(input_pdf, output_pdf, metadata_dict):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata(metadata_dict)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"[META] Added metadata and saved as: {output_pdf}\n")

# MAIN PROGRAM
if __name__ == "__main__":
    # Example PDFs (change these to your files)
    pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

    # 1️⃣ Merge PDFs
    merge_pdfs(pdf_files, "merged.pdf")

    # 2️⃣ Split PDF
    split_pdf("merged.pdf")

    # 3️⃣ Extract Text
    extract_text("merged.pdf")

    # 4️⃣ Rotate page 1 of merged.pdf by 90 degrees
    rotate_page("merged.pdf", page_number=1, degrees=90, output_pdf="rotated.pdf")

    # 5️⃣ Add Metadata
    metadata = {
        "/Title": "My Merged PDF",
        "/Author": "Aditya",
        "/Subject": "PDF Manipulation Demo",
        "/Creator": "Python pypdf"
    }
    add_metadata("merged.pdf", "merged_with_metadata.pdf", metadata)
