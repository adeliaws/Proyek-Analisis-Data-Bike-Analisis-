import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Proyek Analisis Data')
st.write('Adelia Wahyu Suryandari')

day_df = pd.read_csv("https://raw.githubusercontent.com/adeliaws/Proyek-Analisis-Data-Bike-Analisis-/main/data/day.csv", delimiter=",")

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

day_data = {'weekday': ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'],
            'casual': [10, 15, 20, 25, 30, 35, 40],
            'registered': [20, 25, 30, 35, 40, 45, 50]}

day_df = pd.DataFrame(day_data)

hari = day_df['weekday']
Casual = day_df['casual']
Registered = day_df['registered']

# Create a Streamlit app
st.title("Number of Students in each group")

fig, ax = plt.subplots()
X_axis = np.arange(len(hari))

ax.bar(X_axis - 0.2, Casual, 0.4, label='Casual')
ax.bar(X_axis + 0.2, Registered, 0.4, label='Registered')

ax.set_xticks(X_axis)
ax.set_xticklabels(hari)
ax.set_xlabel("Hari")
ax.set_ylabel("Banyak Sepeda Dipinjam")
ax.set_title("Number of Students in each group")
ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')

# Display the plot using Streamlit
st.pyplot(fig)

# Visualisasi pengaruh pelanggan casual dan registered per season
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
