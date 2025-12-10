import re

class Extractor:
    def __init__(self):
        # Patterns common to invoices/receipts
        self.date_pattern = re.compile(r"\b\d{1,2}\s*(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)[,]?\s*\d{4}\b")
        self.total_pattern = re.compile(r"(?i)total\s*[:\-]?\s*\$?\d+(?:[\.,]\d{2})?")

    def extract_fields(self, raw_text, doc_type):
        if doc_type == "invoice":
            return self.extract_invoice(raw_text)
        elif doc_type == "receipt":
            return self.extract_receipt(raw_text)
        elif doc_type == "contract":
            return self.extract_contract(raw_text)
        else:
            return {}
        
    def extract_invoice(self, raw_text):
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        
        date = self.date_pattern.findall(raw_text)
        date = date[0] if date else None

        total = None
        total_match = self.total_pattern.search(raw_text)
        if total_match:
            amount = re.search(r"\$?\d+(?:[\.,]\d{2})?", total_match.group())
            if amount:
                total = amount.group()

        # Vendor
        vendor = None
        for i, line in enumerate(lines):
            if "from:" in line.lower() and i + 1 < len(lines):
                vendor = lines[i + 1]
                break
        if not vendor and lines:
            vendor = lines[0]
        return {"date": date, "total_amount": total, "vendor_name": vendor}
    
    def extract_receipt(self, raw_text):
        # Example: receipts usually have date, total, store name
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        date = self.date_pattern.findall(raw_text)
        date = date[0] if date else None
        total = None
        total_match = self.total_pattern.search(raw_text)
        if total_match:
            amount = re.search(r"\$?\d+(?:[\.,]\d{2})?", total_match.group())
            if amount:
                total = amount.group()
        store_name = lines[0] if lines else None  # assume first line is store
        return {"date": date, "total_amount": total, "store_name": store_name}

    def extract_contract(self, raw_text):
        # Example: contracts usually have parties and dates
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        date = self.date_pattern.findall(raw_text)
        date = date[0] if date else None
        parties = []
        for line in lines[:10]:  # look in the first few lines
            if "party" in line.lower() or "agreement with" in line.lower():
                parties.append(line)
        return {"date": date, "parties": parties if parties else None}
    

if __name__ == "__main__":
    raw_text = """YOUR
        LOGO

        INVOICE

        Date: 02 June, 2030

        Billed to:

        Studio Shodwe

        123 Anywhere St., Any City
        hello@reallygreatsite.com

        Item

        Logo
        Banner (2x6m)

        Poster (1x2m)

        Payment method: Cash

        Quantity

        Note: Thank you for choosing us!

        NO. 000001

        From:

        Olivia Wilson

        123 Anywhere St., Any City
        hello@reallygreatsite.com

        Price Amount
        $500 $500
        $45 $90
        $55 $165
        Total $755"""

    obj = Extractor()
    print(obj.extract_fields(raw_text=raw_text, doc_type="invoice"))
            