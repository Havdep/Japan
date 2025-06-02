import pdfplumber
import os # Import the os module to use os.path.basename later

# Define the path to your PDF file
pdf_path = r"C:\Users\ASUS\OneDrive\Desktop\resume.pdf"

# Check if the file exists first (good practice!)
if not os.path.exists(pdf_path):
    print(f"Error: The file '{os.path.basename(pdf_path)}' was not found at '{pdf_path}'. Please check the path and filename.")
else:
    print(f"Attempting to open PDF: {os.path.basename(pdf_path)}")
    try:
        # Open the PDF using a 'with' statement for proper handling
        with pdfplumber.open(pdf_path) as pdf:
            # Print the total number of pages found
            print(f"Total pages in PDF: {len(pdf.pages)}")

            # Loop through each page object in the 'pdf.pages' list
            for page_num, page in enumerate(pdf.pages):
                # 'page_num' is the 0-indexed page number (e.g., 0 for the first page)
                # 'page' is the actual pdfplumber Page object for the current page

                # Print a header for each page's content
                print(f"\n--- Content from Page {page_num + 1} ---") # Add 1 for human-readable page number

                # Extract all text from the current page
                text = page.extract_text()

                if text:
                    print(text.strip()) # .strip() removes any leading/trailing whitespace
                else:
                    print(f"No text found on Page {page_num + 1}.")

            print("\nSuccessfully extracted text from all pages.")

    except Exception as e:
        # Catch any errors that might occur during PDF processing
        print(f"An error occurred while processing the PDF: {e}")