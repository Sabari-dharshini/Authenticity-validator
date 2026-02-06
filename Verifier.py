import json

def verify_certificate(extracted_text):
    with open("sample_data/valid_certificates.json") as f:
        records = json.load(f)

    score = 0
    reasons = []

    for field in ["University", "Degree", "Registration"]:
        if field.lower() in extracted_text.lower():
            score += 25
        else:
            reasons.append(f"{field} mismatch")

    return score, reasons
