from fastapi import FastAPI, File, UploadFile

from src.preprocessor import Preprocessor
from src.ocr_engine import OCREngine
from src.extractor import Extractor
from src.classifier import Classifier

app = FastAPI()

preprocessor = Preprocessor()
ocr_engine = OCREngine()
classifier = Classifier()
extractor = Extractor()

@app.post("/process_document")
async def process_document(file: UploadFile = File(...)):
    file_path = f"/tmp/{file.filename}"
    with open(file_path, 'wb') as f:
        f.write(file.file.read())

    #pipeline
    image = preprocessor.preprocess(file_path)
    ocr_result = ocr_engine.run_ocr(image)
    doc_type = classifier.classify_test(ocr_result["raw_text"])
    fields = extractor.extract_fields(doc_type=doc_type, raw_text=ocr_result["raw_text"])

    return {
        "document_type": doc_type,
        "fields": fields,
        "ocr_text": ocr_result["raw_text"]
    }