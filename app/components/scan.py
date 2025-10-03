import pytesseract
from PIL import Image
import pypdfium2 as pdfium
import io
import os


# --- Configuration ---
# IMPORTANT: You must set the path to the Tesseract executable
# if it is not automatically found by pytesseract.
#
# Example for Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def ocr_scanned_pdf(pdf_path: str) -> str:
    """
    Performs OCR on a scanned PDF file and returns the extracted text.

    Args:
        pdf_path: The file path to the scanned PDF.

    Returns:
        A string containing all text extracted from the PDF,
        or an error message if the file cannot be processed.
    """
    if not os.path.exists(pdf_path):
        return f"Error: PDF file not found at {pdf_path}"

    try:
        # Load the PDF file using pypdfium2
        pdf_document = pdfium.PdfDocument(pdf_path)
        num_pages = len(pdf_document)
        full_text = []

        print(f"Starting OCR on {num_pages} pages...")

        for i in range(num_pages):
            page = pdf_document.get_page(i)

            # Render the page to a bitmap (image)
            # Scale factor 2 provides good resolution for OCR
            bitmap = page.render(scale=2)

            # Convert the bitmap to a PIL Image object
            image = bitmap.to_pil()

            # --- OCR Processing ---
            # Use pytesseract to extract text from the image
            text = pytesseract.image_to_string(image)

            print(f"--- Page {i+1} OCR Completed ---")
            full_text.append(text)

        return "\n".join(full_text)

    except pytesseract.TesseractNotFoundError:
        return "Error: Tesseract is not installed or not in your PATH. Please install it or set 'pytesseract.pytesseract.tesseract_cmd'."
    except Exception as e:
        return f"An error occurred during processing: {e}"
