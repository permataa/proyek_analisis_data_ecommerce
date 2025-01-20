# E-Commerce Data Analysis Dashboard ✨
Dashboard ini dibuat untuk membantu menganalisis data e-commerce, menggali insight dari data, dan memberikan visualisasi interaktif untuk mendukung pengambilan keputusan bisnis.

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Fitur
Dashboard ini memiliki fitur berikut:

1. Analisis Produk Terlaris :
	Visualisasi produk-produk yang memiliki penjualan tertinggi berdasarkan data yang tersedia.
2. Filter Berdasarkan Tanggal :
	Pilihan untuk memfilter data berdasarkan rentang waktu tertentu.
3. Visualisasi Top Kategori Produk :
	Analisis kategori produk berdasarkan jumlah penjualan.
4. Tema Warna Interaktif :
	Pilihan untuk mengubah tema warna visualisasi sesuai preferensi pengguna.
5. Unduh Data yang Difilter :
	Data yang difilter dapat diunduh dalam format CSV untuk keperluan analisis lebih lanjut.

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```


## Cara Menjalankan
1. Clone Repository
Clone repository ini menggunakan perintah berikut:
git clone https://github.com/permataa/proyek_analisis_data_ecommerce.git
2. Masuk ke Direktori Repository
Pindah ke direktori project yang telah di-clone:
cd dashboard
3. Install Dependencies
Pastikan sudah menginstall Python (versi 3.8 atau lebih baru) dan pip di sistem. Lalu, install pustaka Python yang diperlukan dengan perintah:
pip install -r requirements.txt
4. Jalankan Aplikasi
Jalankan aplikasi Streamlit menggunakan perintah berikut:
streamlit run dashboard.py
5. Akses Aplikasi
Setelah perintah di nomor 4 dijalankan, aplikasi akan terbuka di browser pada alamat:
http://localhost:8501
Jika dijalankan di server, gunakan IP atau domain server.

## Cara Mengakses Versi Online
Aplikasi ini juga tersedia secara online dan dapat diakses melalui link berikut: https://strmlit-proyek1.streamlit.app/







