import streamlit as st
import pickle

# Load model
model = pickle.load(open('insurance_model.sav', 'rb'))

# Judul
st.title('Prediksi Estimasi Biaya Asuransi Kesehatan')

# Inputan pengguna
age = st.number_input('Umur (age)', min_value=0)
bmi = st.number_input('BMI (Body Mass Index)', min_value=0.0)
smoker = st.selectbox('Apakah perokok?', ['Tidak', 'Ya'])

# Konversi smoker jadi angka (seperti training model)
smoker_val = 1 if smoker == 'Ya' else 0

# Prediksi biaya
prediction = ''
if st.button('Prediksi Biaya'):
    biaya = model.predict([[age, bmi, smoker_val]])
    prediction = f"Estimasi biaya asuransi: ${biaya[0]:,.2f}"
    st.success(prediction)