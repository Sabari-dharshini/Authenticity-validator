def calculate_confidence(ocr_score, db_score):
    confidence = (ocr_score * 0.4) + (db_score * 0.6)
    return round(confidence, 2)
