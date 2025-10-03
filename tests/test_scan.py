from app.components.scan import *


def test_scan():
    # --- Example Usage ---
    # Replace 'path/to/your/scanned_document.pdf' with your actual file path
    pdf_file = "./sample_forms/property_personal/Acord-80-Personal-Property-filled.pdf"

    # --- IMPORTANT: Ensure you have a scanned PDF file here for testing ---
    # For demonstration, we'll use a placeholder path:
    # If you want to test this, create a simple PDF with a picture of text.

    # Example using a dummy file path (update this):
    # dummy_pdf_file = "sample_scanned_document.pdf"

    # Assuming 'sample_scanned_document.pdf' exists and is a scanned image PDF
    if os.path.exists(pdf_file):
        extracted_text = ocr_scanned_pdf(pdf_file)

        print("\n====================================")
        print("         EXTRACTED TEXT")
        print("====================================\n")
        print(extracted_text)
    else:
        print(
            f"Please replace '{pdf_file}' with the path to an existing scanned PDF to run the example."
        )
