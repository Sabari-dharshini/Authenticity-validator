import easyocr
reader = easyocr.Reader(['en'])

result = reader.readtext(image)
extracted_text = " ".join([text for _, text, _ in result])

