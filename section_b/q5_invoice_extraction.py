import re
import json

def extract_text():
    """
    Simulating text extraction from a PDF invoice.
    """
    return """
    Invoice Number: INV-2026-001
    Invoice Date: 08-07-2026
    Vendor: ABC Steel Pvt Ltd
    Total Amount: 48490
    """

def llm_extract_fields(text):
    """
    Simulating an LLM extracting structured fields.
    """

    data = {
        "invoice_number": re.search(r"Invoice Number:\s*(.+)", text).group(1),
        "invoice_date": re.search(r"Invoice Date:\s*(.+)", text).group(1),
        "vendor_name": re.search(r"Vendor:\s*(.+)", text).group(1),
        "total_amount": re.search(r"Total Amount:\s*(.+)", text).group(1)
    }

    return data


def main():

    invoice_text = extract_text()
    extracted_data = llm_extract_fields(invoice_text)
    
    print(json.dumps(extracted_data, indent=4))

if __name__ == "__main__":
    main()