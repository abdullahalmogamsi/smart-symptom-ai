
import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import pickle

# الأعراض المستخدمة
symptoms = [
    'fever', 'cough', 'fatigue', 'shortness_of_breath', 'headache',
    'vomiting', 'dizziness', 'muscle_pain', 'chest_pain', 'diarrhea',
    'confusion', 'neck_stiffness', 'joint_pain'
]

# تحميل النموذج والـ label encoder
model = pickle.load(open('xgb_model.pkl', 'rb'))
le = pickle.load(open('label_encoder.pkl', 'rb'))

# واجهة Streamlit
st.title("SmartSymptom AI 👩‍⚕️🧠")
st.subheader("حدد الأعراض التي تشعر بها:")

user_input = []

# بناء مدخلات المستخدم
for symptom in symptoms:
    val = st.checkbox(symptom.replace('_', ' ').capitalize())
    user_input.append(1 if val else 0)

# زر التنبؤ
if st.button("تحليل الأعراض"):
    input_df = pd.DataFrame([user_input], columns=symptoms)
    prediction = model.predict(input_df)
    disease_en = le.inverse_transform(prediction)[0]
    
    # الترجمة اليدوية
    disease_ar_dict = {
        'Flu': 'الإنفلونزا', 'COVID-19': 'كورونا', 'Heatstroke': 'ضربة شمس',
        'Heat Exhaustion': 'الإجهاد الحراري', 'Food Poisoning': 'تسمم غذائي',
        'Asthma Attack': 'نوبة ربو', 'Meningitis': 'التهاب السحايا',
        'Dengue Fever': 'حمى الضنك', 'Dehydration': 'الجفاف', 'Healthy': 'سليم'
    }
    st.success(f"🩺 التشخيص المحتمل: **{disease_en}** ({disease_ar_dict.get(disease_en)})")
