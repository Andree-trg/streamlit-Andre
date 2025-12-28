import streamlit as st
 
st.title('Belajar Analisis Data')

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================
# i. TITLE
# =====================
st.title("Tugas Pertemuan 12 - Web Page Streamlit")

# =====================
# ii. HEADER
# =====================
st.header("Dashboard Sederhana Analisis Data")

# =====================
# iii. SUBHEADER
# =====================
st.subheader("Contoh Implementasi Komponen Streamlit")

# =====================
# iv. CAPTION
# =====================
st.caption("Dibuat menggunakan Python dan Streamlit")

# =====================
# vi. TEXT (Paragraf)
# =====================
st.write("""
Aplikasi web ini dibuat untuk memenuhi tugas pertemuan 12.
Pada halaman ini ditampilkan beberapa komponen utama Streamlit,
mulai dari teks, potongan kode, hingga visualisasi data dalam
bentuk tabel dan grafik.
""")

# =====================
# v. CODE (Potongan Code)
# =====================
st.subheader("Contoh Potongan Kode Python")
st.code("""
import pandas as pd

data = {
    'Tahun': [2021, 2022, 2023, 2024],
    'Penjualan': [150, 200, 250, 300]
}

df = pd.DataFrame(data)
""", language="python")

# =====================
# vii. DATA DISPLAY
# a. TABEL / DATAFRAME
# =====================
st.subheader("Tabel Data Penjualan")

data = {
    'Tahun': [2021, 2022, 2023, 2024],
    'Penjualan': [150, 200, 250, 300]
}
df = pd.DataFrame(data)

st.dataframe(df)

# =====================
# vii. DATA DISPLAY
# b. CHART
# =====================
st.subheader("Grafik Penjualan per Tahun")

fig, ax = plt.subplots()
ax.plot(df['Tahun'], df['Penjualan'], marker='o')
ax.set_xlabel("Tahun")
ax.set_ylabel("Penjualan")
ax.set_title("Grafik Penjualan Tahunan")

st.pyplot(fig)
