
import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import pickle

# Load model and encoder
model = pickle.load(open("xgb_model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# Symptoms list
symptoms = [
    ("Fever", "حمى"), ("Cough", "سعال"), ("Fatigue", "إرهاق"), ("Shortness of breath", "ضيق تنفس"),
    ("Headache", "صداع"), ("Vomiting", "قيء"), ("Dizziness", "دوخة"), ("Muscle pain", "ألم في العضلات"),
    ("Chest pain", "ألم في الصدر"), ("Diarrhea", "إسهال"), ("Confusion", "ارتباك"),
    ("Neck stiffness", "تصلب في الرقبة"), ("Joint pain", "ألم في المفاصل")
]

# --- CSS Styling ---
st.markdown("""
    <style>
    body { background-color: #f5f5f5; }
    .main { background-color: #111827; color: white; }
    .stButton > button {
        background-color: #10b981;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 0.5em 1.5em;
    }
    .checkbox-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.5rem;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and Header ---
st.markdown("<h1 style='text-align:center;'>🧠 SmartSymptom AI</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>حدد الأعراض التي تشعر بها:</h3>", unsafe_allow_html=True)

# --- Symptoms Form ---
user_input = []
cols = st.columns(2)

for i, (en, ar) in enumerate(symptoms):
    col = cols[i % 2]
    val = col.checkbox(f"{ar} / {en}")
    user_input.append(1 if val else 0)

# --- Prediction ---
if st.button("تحليل الأعراض"):
    input_df = pd.DataFrame([user_input], columns=[s[0].lower().replace(" ", "_") for s in symptoms])
    prediction = model.predict(input_df)
    disease_en = le.inverse_transform(prediction)[0]

    # Disease translation
    disease_ar_dict = {
        'Flu': 'الإنفلونزا', 'COVID-19': 'كورونا', 'Heatstroke': 'ضربة شمس',
        'Heat Exhaustion': 'الإجهاد الحراري', 'Food Poisoning': 'تسمم غذائي',
        'Asthma Attack': 'نوبة ربو', 'Meningitis': 'التهاب السحايا',
        'Dengue Fever': 'حمى الضنك', 'Dehydration': 'الجفاف', 'Healthy': 'سليم'
    }

    st.success(f"🩺 التشخيص المحتمل: **{disease_en}** ({disease_ar_dict.get(disease_en)})")
