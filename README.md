
# SmartSymptom AI 🤖🩺  
**الذكاء الاصطناعي لتشخيص الأعراض**

SmartSymptom AI is a lightweight, AI-powered web application that predicts potential medical conditions based on user-reported symptoms.
سمارت سمبتوم AI هو تطبيق ويب ذكي وخفيف، يتنبأ بالحالات الصحية المحتملة بناءً على الأعراض التي يحددها المستخدم.

---

## 🌟 Features | الميزات

- ✅ Predicts 10 common conditions including flu, COVID-19, dehydration, and heatstroke.  
  يتعرف على 10 أمراض شائعة مثل الإنفلونزا، كورونا، الجفاف، وضربة الشمس.

- ✅ Interactive symptom checklist interface (built with Streamlit).  
  واجهة تفاعلية بسيطة لاختيار الأعراض (باستخدام Streamlit).

- ✅ Supports bilingual output (Arabic and English diagnosis).  
  يدعم عرض التشخيص باللغتين العربية والإنجليزية.

- ✅ Lightweight and runs locally without an internet connection.  
  خفيف ويعمل محليًا بدون الحاجة إلى الإنترنت.

- ✅ Model trained on synthetic symptom data using XGBoost.  
  النموذج مدرّب باستخدام بيانات اصطناعية واقعية مع XGBoost.

---

## 🧠 Use Case | حالات الاستخدام

- Pilgrims during Hajj and Umrah  
  الحجاج خلال موسمي الحج والعمرة  
- Healthcare staff in crowd environments  
  الكوادر الطبية في الأماكن المزدحمة  
- Emergency symptom triage scenarios  
  سيناريوهات الطوارئ والفرز الأولي للأعراض

---

## 🛠️ Tech Stack | التقنيات المستخدمة

- Python 3
- Streamlit
- XGBoost
- Scikit-learn
- Pandas + NumPy

---

## 🚀 Getting Started | خطوات التشغيل

### 1. Clone or download the project  
### ١. قم بتنزيل المشروع أو نسخه
```bash
git clone https://github.com/YOUR_USERNAME/smart-symptom-ai.git
cd smart-symptom-ai
```

### 2. Install dependencies  
### ٢. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

### 3. Run the app  
### ٣. تشغيل التطبيق
```bash
streamlit run app.py
```

---

## 📂 Files Overview | نظرة على الملفات

| الملف | الوظيفة |
|-------|---------|
| `app.py` | واجهة Streamlit لتشخيص الأعراض |
| `xgb_model.pkl` | النموذج المدرب باستخدام XGBoost |
| `label_encoder.pkl` | محول أسماء الأمراض |
| `requirements.txt` | قائمة المكتبات المطلوبة للتشغيل |

---

## 📊 Example | مثال

User selects:  
المستخدم يختار:  
- `Fever`, `Fatigue`, `Headache`, `Dizziness`

Model output:  
النموذج يتوقع:  
> **Predicted Condition**: Flu (الإنفلونزا)

---

## 📄 License | الرخصة

This project is for academic and hackathon use. Free to use with attribution.  
هذا المشروع للاستخدام الأكاديمي وفي المسابقات، ومتاح مجانًا مع الإشارة للمصدر.

---

## 🤝 Acknowledgements | الشكر والتقدير

This app was built as part of the **Hajj Health and Safety Hackathon**.  
تم بناء هذا التطبيق كجزء من **هاكاثون الصحة والسلامة في الحج**.
