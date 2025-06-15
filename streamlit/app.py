import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load data and model
st.set_page_config(page_title="Deteksi Dropout Siswa", page_icon="🎓", layout="wide")

df = pd.read_csv("./cleaned.csv")
model = joblib.load("./model/student_dropout_model.joblib")

# Sidebar for branding and info
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/000000/graduation-cap.png", width=80)
    st.title("Jaya Jaya Institut")
    st.markdown("""
    **Sistem Deteksi Dropout**
    
    Aplikasi ini membantu mendeteksi potensi siswa yang akan dropout sehingga dapat diberikan bimbingan khusus.
    """)
    st.markdown("---")
    st.info("Silakan isi data siswa di sebelah kanan.")

# Main Title
st.markdown("<h1 style='text-align: center; color: #4F8BF9;'>🎓 Klasifikasi Deteksi Potensi Dropout Pada Siswa</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Sistem ini bertujuan untuk mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus pada <b>Jaya Jaya Institut</b>.</p>", unsafe_allow_html=True)
st.markdown("---")

# Prepare unique values
curricular_units_2nd_sem_approved = df["Curricular_units_2nd_sem_approved"].unique()
curricular_units_1st_sem_approved = df["Curricular_units_1st_sem_approved"].unique()
curricular_units_2nd_sem_enrolled = df["Curricular_units_2nd_sem_enrolled"].unique()
curricular_units_2nd_sem_evaluations = df["Curricular_units_2nd_sem_evaluations"].unique()
curricular_units_1st_sem_enrolled = df["Curricular_units_1st_sem_enrolled"].unique()

# Input Form
with st.form("input_form", clear_on_submit=False):
    st.subheader("📝 Data Akademik Siswa")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        opt_curricular_units_1st_sem_approved = st.selectbox(
            "Jumlah satuan kurikulum yang disetujui pada semester pertama",
            np.sort(curricular_units_1st_sem_approved))
        opt_curricular_units_1st_sem_enrolled = st.selectbox(
            "Jumlah satuan mata kuliah yang diambil pada semester pertama",
            np.sort(curricular_units_1st_sem_enrolled))
        opt_curricular_units_2st_sem_approved = st.selectbox(
            "Jumlah satuan kurikulum yang disetujui pada semester kedua",
            np.sort(curricular_units_2nd_sem_approved))
        opt_curricular_units_2nd_sem_enrolled = st.selectbox(
            "Jumlah satuan mata kuliah yang diambil pada semester kedua",
            np.sort(curricular_units_2nd_sem_approved))
        opt_curricular_units_2nd_sem_evulations = st.selectbox(
            "Jumlah satuan kurikulum yang dievaluasi pada semester kedua",
            np.sort(curricular_units_2nd_sem_evaluations))
    with col2:
        val_curricular_units_1st_grade = st.number_input(
            "Nilai rata-rata semester pertama", min_value=0, max_value=18)
        val_curricular_units_2nd_grade = st.number_input(
            "Nilai rata-rata semester kedua", min_value=0, max_value=18)
        opt_tuition_fees_up_to_date = st.radio(
            "Biaya kuliah siswa sudah sesuai dengan yang berlaku",
            options=["Tidak Sesuai", "Sesuai"])
        opt_scholarship_holder = st.radio(
            "Siswa memiliki beasiswa", options=["Tidak", "Ya"])
        opt_displaced = st.radio(
            "Siswa merupakan orang terlantar", options=["Tidak", "Ya"])
    st.markdown("---")
    submitted = st.form_submit_button("🔍 Prediksi Dropout", use_container_width=True)

if submitted:
    predict_df = pd.DataFrame({
        "Curricular_units_2nd_sem_approved": opt_curricular_units_2st_sem_approved,
        "Curricular_units_2nd_sem_grade": val_curricular_units_2nd_grade,
        "Curricular_units_1st_sem_approved": opt_curricular_units_1st_sem_approved,
        "Curricular_units_1st_sem_grade": val_curricular_units_1st_grade,
        "Tuition_fees_up_to_date": 0 if opt_tuition_fees_up_to_date == "Tidak Sesuai" else 1,
        "Scholarship_holder": 0 if opt_scholarship_holder == "Tidak" else 1,
        "Curricular_units_2nd_sem_enrolled": opt_curricular_units_2nd_sem_enrolled,
        "Curricular_units_1st_sem_enrolled": opt_curricular_units_1st_sem_enrolled,
        "Curricular_units_2nd_sem_evaluations": opt_curricular_units_2nd_sem_evulations,
        "Displaced": 0 if opt_displaced == "Tidak" else 1
    }, index=[0])

    predict = model.predict_proba(predict_df)
    predict_proba = model.predict_proba(predict_df)[0]
    predict_proba = [round(x*100, 2) for x in predict_proba]
    labels = ['Dropout', 'Tidak Dropout']
    probability_metrics = pd.DataFrame(
        {"Kelas": labels, "Probabilitas": predict_proba}, columns=["Kelas", "Probabilitas"])

    st.markdown("---")
    pred_label = labels[np.argmax(predict)]
    if pred_label == 'Dropout':
        st.error(f"🚨 Prediksi: {pred_label}", icon="🚨")
    else:
        st.success(f"✅ Prediksi: {pred_label}", icon="✅")
    st.markdown("### Probabilitas Setiap Kelas:")
    st.table(probability_metrics)
    st.info("Interpretasi: Semakin tinggi probabilitas pada kelas 'Dropout', semakin besar risiko siswa untuk keluar.")