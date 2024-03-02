# Import library yang akan digunakan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca data dari CSV
all_df = pd.read_csv("three_stations.csv")
all_df['timestamp'] = pd.to_datetime(all_df['timestamp'])

# Menentukan title dari dashboard
st.title("Projek Akhir Analisis Data - Dicoding :sparkles:")

# Membuat layouting berupa tab untuk menampilkan visual data
tab1, tab2 = st.tabs(["PM2.5", "PM10"])

# Visual data yang ditampilkan di tab akan ditampung pada sebuah container
with st.container():
    # Membuat visual data pada tab pertama
    with tab1 :
        st.header("Perbandingan AQI(Air Quality Index) PM2.5 di Setiap Stasiun")
        fig = plt.figure(figsize=(12, 7))
        sns.boxplot(x="station", y="AQI_PM2.5", data=all_df)
        plt.title("Boxplot AQI PM2.5 di Setiap Stasiun")
        plt.xlabel("Timestamp")
        plt.ylabel("Stasiun")
        st.pyplot(fig)

    # Membuat visual data pada tab kedua
    with tab2 :
        st.header("Perbandingan AQI(Air Quality Index) PM10 di Setiap Stasiun")
        fig = plt.figure(figsize=(12, 7))
        sns.boxplot(x="station", y="AQI_PM10", data=all_df)
        plt.title("Boxplot AQI PM10 di Setiap Stasiun")
        plt.xlabel("Timestamp")
        plt.ylabel("Stasiun")
        st.pyplot(fig)

# Membuat subheader, untuk menampilkan rumus perhitungan AQI yang digunakan
st.subheader("Rumus untuk Memperoleh AQI Adalah")
st.latex(r"""
AQI = \left( \frac{(AQI_{\text{max}} - AQI_{\text{min}})}{(C_{\text{max}} - C_{\text{min}})} \right) \times (C - C_{\text{min}}) + AQI_{\text{min}}
""")

# Membuat sebuah expander untuk menampilkan informasi tambahan mengenai rumus yang telah dijabarkan diatas
with st.expander("Keterangan yang digunakan dalam rumus :"):
    st.write("""
            - Standar AQI yang digunakan yaitu AQI Tiongkok (China's Air Quality Index).
            - C adalah konsentrasi polutan yang diukur (misalnya, PM2.5 dalam µg/m³).
            - Cmin dan Cmax adalah batas bawah dan atas konsentrasi polutan untuk kategori AQI yang bersangkutan.
            - AQImin dan AQImax adalah nilai AQI minimum dna maksimum untuk kategori tersebut.     
             """)

# Membuat sebuah header untuk melakukan visual data "Status AQI"
st.header("Mengklasifikasikan dan Melihat Jumlah dari Status AQI ")
tab1, tab2 = st.tabs(["Status AQI PM2.5", "Status AQI PM10"])

# Tahap ini telah dilakukan di colab sebelumnya, tetapi dilakukan lagi agar tidak ada error dan dataframe bisa digunakan di file .py
classification_counts_pm25 = all_df.groupby("Status_AQI_PM2.5").size()
classification_counts_pm10 = all_df.groupby("Status_AQI_PM10").size()

# Membuat container untuk menampung tab yang berisi visual data
with st.container():
    # Membuat visual data pada tab pertama
    with tab1:
        st.header("Status AQI PM2.5")
        fig, ax = plt.subplots()
        ax.bar(classification_counts_pm25.index, classification_counts_pm25.values)
        plt.xticks(rotation=45)
        plt.ylabel("Count pada ketiga stasiun")
        plt.xlabel("Status AQI")
        st.pyplot(fig)
    
    # Membuat visual data pada tab kedua
    with tab2:
        st.header("Status AQI PM10")
        fig, ax = plt.subplots()
        ax.bar(classification_counts_pm10.index, classification_counts_pm10.values)
        plt.xticks(rotation=45)
        plt.ylabel("Count pada ketiga stasiun")
        plt.xlabel("Status AQI")
        st.pyplot(fig)
    