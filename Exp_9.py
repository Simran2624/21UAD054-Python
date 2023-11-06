import pdfplumber

pdf_file = 'foo.pdf'

# Open the PDF file
with pdfplumber.open(pdf_file) as pdf:
    for page_number, page in enumerate(pdf.pages):
        # Extract tables from the page
        tables = page.extract_tables()

        # Iterate through extracted tables on the current page
        for table_number, table in enumerate(tables):
            print(f"Table {table_number + 1} on Page {page_number + 1}:")

            # Iterate through rows in the table
            for row in table:
                # Print the row as a list of cells
                print(row)

            # Add a separator for clarity
            print("-" * 20)
