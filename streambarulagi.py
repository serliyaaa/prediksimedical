import streamlit as st
import pickle
import os

st.write("Current working directory:", os.getcwd())  # Untuk cek lokasi kerja saat ini

model = pickle.load(open('insurance_model.sav', 'rb'))


# Setup awal
st.set_page_config(page_title="Estimasi Biaya Asuransi", layout="wide")

# Simpan data riwayat prediksi
if 'riwayat' not in st.session_state:
    st.session_state.riwayat = []

# Sidebar kayak menu resepsionis
st.sidebar.title("🏥 Menu Navigasi")
menu = st.sidebar.radio("Pilih halaman:", ["Form Prediksi", "Riwayat Prediksi"])

# Halaman 1: Form Prediksi
if menu == "Form Prediksi":
    st.title('🧾 Prediksi Estimasi Biaya Asuransi Kesehatan')

    # Inputan pengguna
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input('Umur (age)', min_value=0, step=1)
        bmi = st.number_input('BMI (Body Mass Index)', min_value=0.0, step=0.1)
    with col2:
        smoker = st.selectbox('Apakah perokok?', ['Tidak', 'Ya'])

    # Konversi smoker jadi angka
    smoker_val = 1 if smoker == 'Ya' else 0

    # Prediksi biaya
    if st.button('🔍 Prediksi Biaya'):
        biaya = model.predict([[age, bmi, smoker_val]])
        hasil = f"💰 Estimasi biaya asuransi: **${biaya[0]:,.2f}**"
        st.success(hasil)

        # Simpan ke riwayat
        st.session_state.riwayat.append({
            'Umur': age,
            'BMI': bmi,
            'Perokok': smoker,
            'Estimasi Biaya': f"${biaya[0]:,.2f}"
        })

# Halaman 2: Riwayat
elif menu == "Riwayat Prediksi":
    st.title('📋 Riwayat Prediksi Biaya Asuransi')
    if st.session_state.riwayat:
        df_riwayat = pd.DataFrame(st.session_state.riwayat)
        st.dataframe(df_riwayat)
    else:
        st.info("Belum ada prediksi. Coba isi dulu di menu 'Form Prediksi'~")
