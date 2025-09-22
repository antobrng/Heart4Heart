from PyPDF2 import PdfReader, PdfWriter

input_pdf = "/Users/antoninberanger/Documents/Heart4Heart/files/all_café_campus_tickets.pdf"
output_folder = "/Users/antoninberanger/Documents/Heart4Heart/files/individual_pdfs"

reader = PdfReader(input_pdf)

for i in range(len(reader.pages)):
    writer = PdfWriter()
    writer.add_page(reader.pages[i])

    output_filename = f"/Users/antoninberanger/Documents/Heart4Heart/files/individual_pdfs/ticket_{i+1:03}.pdf"
    with open(output_filename, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Saved {output_filename}")

print("All pages have been split and saved as individual PDFs.")

