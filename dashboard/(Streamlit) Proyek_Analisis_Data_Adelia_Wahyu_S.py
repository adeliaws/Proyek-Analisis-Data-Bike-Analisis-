import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Proyek Analisis Data')
st.write('Adelia Wahyu Suryandari')

day_df = pd.read_csv("day.csv", delimiter=",")

#Pertanyaan 1

#Trend Harian
trend_harian = day_df.groupby('dteday')['cnt'].mean()

#Grafik "Tren Peminjaman Sepeda Harian"
st.subheader('Tren Peminjaman Sepeda Harian')
fig_trend_harian = plt.figure(figsize=(16, 6))
sns.lineplot(x=trend_harian.index, y=trend_harian.values)
plt.title('Tren Peminjaman Sepeda Harian')
plt.xlabel('Tanggal')
plt.ylabel('Rata-rata Jumlah Peminjaman')
plt.xticks(rotation=45)
st.pyplot(fig_trend_harian)

#Pertanyaan 2
seasonal_avg = day_df.groupby(['season', 'dteday'])[['casual', 'registered', 'cnt']].mean().reset_index()

# Visualisasi pengaruh pelanggan casual dan registered

# Casual Users
st.subheader('Pengaruh Pelanggan Casual terhadap Rata-rata Peminjaman Sepeda per Hari')
fig_casual = plt.figure(figsize=(16, 8))
sns.barplot(x='dteday', y='casual', hue='season', data=seasonal_avg)
plt.title('Pengaruh Pelanggan Casual terhadap Rata-rata Peminjaman Sepeda per Hari')
st.pyplot(fig_casual)

# Registered Users
st.subheader('Pengaruh Pelanggan Registered terhadap Rata-rata Peminjaman Sepeda per Hari')
fig_registered = plt.figure(figsize=(16, 8))
sns.barplot(x='dteday', y='registered', hue='season', data=seasonal_avg)
plt.title('Pengaruh Pelanggan Registered terhadap Rata-rata Peminjaman Sepeda per Hari')
st.pyplot(fig_registered)
