# Smart Document Analyzer

## Overview
Smart Document Analyzer is a lightweight tool to automatically process documents (PDFs or images), extract text using OCR, classify document types, and extract key information such as dates, amounts, and vendor names. The results can be exported as JSON or CSV.

---

## Features

- Upload PDF or image files
- Preprocess images (resize, denoise, grayscale)
- Extract text using Tesseract OCR
- Rule-based document classification:
  - Invoice
  - Receipt
  - Contract
  - Unknown
- Extract key fields depending on document type:
  - Invoice: date, total_amount, vendor_name
  - Receipt: date, total_amount, store_name
  - Contract: date, parties
- Simple web interface via Streamlit
- API backend via FastAPI

---

## Tech Stack

- **Computer Vision / OCR:** OpenCV, pytesseract  
- **Text Processing:** Python regex, simple heuristics  
- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **Other:** pandas, logging

---
