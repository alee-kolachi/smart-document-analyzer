import pytesseract
import cv2
import pandas as pd

class OCREngine:
    def __init__(self):
        pass
    
    def run_ocr(self, image_path):
        # return raw text + boxes + confidence
        img = cv2.imread(image_path)
        raw_text = pytesseract.image_to_string(img)

        data_df = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME)    
        words_data = data_df[data_df.conf != -1]
        words_data = words_data.dropna(subset = ['text'])

        block_list = []
        for index, row in words_data.iterrows():
            bbox = [row['left'], row['top'], row['left'] + row['width'], row['top'] + row['height']]
            block = {
                "text": row['text'],
                "confidence": int(float(row['conf'])),
                "bbox": bbox
            }
            block_list.append(block)

        output_dict = {
            "raw_text": raw_text.strip(),
            "blocks": block_list
        }
        return output_dict

image_path = "../images/lom.jpg"

obj = OCREngine()
print(obj.run_ocr(image_path)["blocks"])
