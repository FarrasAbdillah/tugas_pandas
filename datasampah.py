import pandas as pd

# Membaca file CSV
pd.set_option('display.max_rows', None)
data = pd.read_csv('ds.csv')
print(data)

# Total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun tertentu
total_2019 = 0
for _, row in data.iterrows():
    if row['tahun'] == 2019:
        total_2019 += row['jumlah_produksi_sampah']

print(f"Jumlah produksi sampah pada tahun tertentu (2019): {total_2019:.1f} ton")

# Data per tahun
jumlah_per_tahun = {}
for _, row in data.iterrows():
    tahun = row['tahun']
    jumlah_per_tahun[tahun] = jumlah_per_tahun.get(tahun, 0) + row['jumlah_produksi_sampah']

# Dataframe untuk hasil per tahun
df_per_tahun = pd.DataFrame(list(jumlah_per_tahun.items()), columns=['Tahun', 'Jumlah Produksi Sampah'])
print(df_per_tahun)

# Data per Kota/Kabupaten per tahun
jmlh_sampah = {}
for _, row in data.iterrows():
    daerah = row["nama_kabupaten_kota"]
    sampah = row["jumlah_produksi_sampah"]
    jmlh_sampah[daerah] = jmlh_sampah.get(daerah, 0) + sampah

print("Data sampah (ton) dari tiap kabupaten/kota:")
for daerah, sampah in jmlh_sampah.items():
    print(f"Jumlah sampah di daerah {daerah} dari tahun 2015 - 2021 adalah {sampah:.1f} ton")

# Dataframe untuk hasil per Kabupaten/Kota
df_per_kota = pd.DataFrame(list(jmlh_sampah.items()), columns=['Kabupaten/Kota', 'Jumlah Produksi Sampah'])
print(df_per_kota)

# Menyimpan hasil ke file CSV dan Excel
df_per_tahun.to_csv('jumlah_sampah_per_tahun.csv', index=False)
df_per_tahun.to_excel('jumlah_sampah_per_tahun.xlsx', index=False)

df_per_kota.to_csv('jumlah_sampah_per_kota.csv', index=False)
df_per_kota.to_excel('jumlah_sampah_per_kota.xlsx', index=False)
