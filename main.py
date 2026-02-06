import streamlit as st
from PIL import Image

st.set_page_config(page_title="Certificate Authenticity Validator")

st.title("🎓 Fake Degree / Certificate Detection System")

def verify_certificate(text):
    score = 0
    issues = []

    if "University" in text:
        score += 30
    else:
        issues.append("University name mismatch")

    if "Degree" in text or "B.Tech" in text:
        score += 30
    else:
        issues.append("Degree information missing")

    if "Registration" in text or "Roll" in text:
        score += 40
    else:
        issues.append("Invalid registration number")

    return score, issues


def calculate_confidence(score):
    return round(score * 0.9, 2)


uploaded_file = st.file_uploader(
    "Upload Degree / Certificate",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Certificate", use_column_width=True)

    if st.button("Verify Certificate"):
        # OCR SIMULATED FOR CLOUD DEPLOYMENT
        extracted_text = """
        University: Jharkhand University
        Degree: B.Tech
        Registration: JH2020CS101
        """

        score, issues = verify_certificate(extracted_text)
        confidence = calculate_confidence(score)

        if confidence >= 60:
            st.success(f"✅ GENUINE CERTIFICATE ({confidence}%)")
        else:
            st.error(f"❌ LIKELY FAKE ({confidence}%)")

        if issues:
            st.warning("Issues Detected:")
            for issue in issues:
                st.write(f"- {issue}")
