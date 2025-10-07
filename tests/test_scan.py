from app.components.scan import *


def test_scan():
    # Example 1: Extract from scanned PDF
    pdf_file = "./sample_forms/property_personal/Acord-80-Personal-Property-filled.pdf"
    output_file = "extracted_text.txt"

    try:
        text = extract_text_from_scanned_pdf(
            pdf_path=pdf_file,
            output_txt_path=output_file,
            dpi=300,  # Higher DPI = better quality
            lang="eng",  # Use 'eng' for English
        )

        # Print first 500 characters
        print("\nExtracted text preview:")
        print(text[:500])

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nTo use this script:")
        print("1. Replace 'scanned_document.pdf' with your PDF file path")
        print("2. Make sure Tesseract and Poppler are installed")

    # Example 2: Extract from image
    # image_file = "scanned_page.png"
    # text = extract_text_from_image(image_file)
    # print(text)
