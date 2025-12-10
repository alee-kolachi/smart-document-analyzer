from src.ocr_engine import OCREngine

class Classifier:
    def __init__(self):
        self.invoice_keywords = ["invoice", "bill", "amount due"]
        self.receipt_keywords = ["receipt", "paid", "change"]
        self.contract_keywords = ["agreement", "contract", "party"]


    def classify_test(self, raw_text):
        text_lower = raw_text.lower()

        if any(keyword in text_lower for keyword in self.invoice_keywords):
            return "invoice"
        elif any(keyword in text_lower for keyword in self.receipt_keywords):
            return "receipt"
        elif any(keyword in text_lower for keyword in self.contract_keywords):
            return "contract"
        else:
            return "unknown"


if __name__ == "__main__":
    image_path = "../images/invoice.webp"
    ocr_object = OCREngine()
    raw_text = ocr_object.run_ocr(image_path=image_path)["raw_text"]
    classifier = Classifier()
    print(classifier.classify_test(raw_text=raw_text))