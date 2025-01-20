import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    return pd.read_csv("data/all_data(2).csv")

# Muat data
data = load_data()

# Sidebar
st.sidebar.title("E-Commerce Dashboard")
selected_analysis = st.sidebar.selectbox(
    "Pilih Analisis", 
    ["Produk Terlaris", "Metode Pembayaran vs Nilai Pesanan", "Lokasi Pelanggan vs Waktu Pengiriman"]
)

# Filter tanggal
st.sidebar.subheader("Filter Tanggal")
start_date = st.sidebar.date_input("Tanggal Mulai", value=datetime(2017, 1, 1))
end_date = st.sidebar.date_input("Tanggal Akhir", value=datetime(2018, 12, 31))

# Filter data berdasarkan tanggal
data['order_purchase_timestamp'] = pd.to_datetime(data['order_purchase_timestamp'])
filtered_data = data[(data['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
                     (data['order_purchase_timestamp'] <= pd.to_datetime(end_date))]

# Pilihan tema warna
st.sidebar.subheader("Pilih Tema Warna")
palette_choice = st.sidebar.selectbox("Tema Warna", ["viridis", "coolwarm", "Blues_d", "magma"])

# Tombol unduh data
def convert_df_to_csv(df):
    output = BytesIO()
    df.to_csv(output, index=False)
    processed_data = output.getvalue()
    return processed_data

if st.sidebar.button("Unduh Data yang Difilter"):
    csv_data = convert_df_to_csv(filtered_data)
    st.sidebar.download_button("Klik untuk Unduh", data=csv_data, file_name="filtered_data.csv", mime="text/csv")

# Judul Dashboard
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>E-Commerce Data Analysis Dashboard</h1>
    <p style='text-align: center;'>Analisis Data E-Commerce untuk Menggali Insights</p>
    """, unsafe_allow_html=True)

if selected_analysis == "Produk Terlaris":
    st.subheader("Produk Apa yang Paling Banyak Terjual?")
    # Produk Terlaris
    top_products = filtered_data.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False).head(10)

    # Visualisasi
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_products.values, y=top_products.index, palette=palette_choice)
    plt.title('Top 10 Produk Terlaris', fontsize=14, fontweight='bold')
    plt.xlabel('Jumlah Terjual', fontsize=12)
    plt.ylabel('Kategori Produk', fontsize=12)
    for index, value in enumerate(top_products.values):
        plt.text(value + 5, index, str(value), va='center')
    st.pyplot(plt)
    st.write("**Kesimpulan:** Kategori produk yang paling banyak terjual adalah 'cama_mesa_banho', diikuti oleh 'beleza_saude' dan 'esporte_lazer'.")
    
elif selected_analysis == "Metode Pembayaran vs Nilai Pesanan":
    st.subheader("Apakah Metode Pembayaran Mempengaruhi Nilai Pesanan?")
    # Rata-rata Nilai Pesanan per Metode Pembayaran
    avg_payment = filtered_data.groupby('payment_type')['price'].mean().sort_values(ascending=False)

    # Visualisasi
    plt.figure(figsize=(10, 6))
    sns.barplot(x=avg_payment.index, y=avg_payment.values, palette=palette_choice)
    plt.title('Rata-rata Nilai Pesanan per Metode Pembayaran', fontsize=14, fontweight='bold')
    plt.xlabel('Metode Pembayaran', fontsize=12)
    plt.ylabel('Rata-rata Nilai Pesanan (BRL)', fontsize=12)
    for index, value in enumerate(avg_payment.values):
        plt.text(index, value + 1, f'{value:.2f}', ha='center')
    st.pyplot(plt)
    st.write("**Kesimpulan:** Kartu kredit digunakan untuk pesanan dengan nilai lebih tinggi dibanding metode pembayaran lainnya seperti debit_card, voucher, dan boleto.")

elif selected_analysis == "Lokasi Pelanggan vs Waktu Pengiriman":
    st.subheader("Apakah Lokasi Pelanggan Mempengaruhi Waktu Pengiriman?")
    # Rata-rata Waktu Pengiriman per Lokasi Pelanggan
    filtered_data['shipping_time'] = pd.to_datetime(filtered_data['order_delivered_customer_date']) - pd.to_datetime(filtered_data['order_purchase_timestamp'])
    avg_shipping_time = filtered_data.groupby('customer_state')['shipping_time'].mean().dt.days

    # Visualisasi
    plt.figure(figsize=(12, 8))
    sns.barplot(x=avg_shipping_time.index, y=avg_shipping_time.values, palette=palette_choice)
    plt.title('Rata-rata Waktu Pengiriman per Lokasi Pelanggan', fontsize=14, fontweight='bold')
    plt.xlabel('Lokasi Pelanggan', fontsize=12)
    plt.ylabel('Rata-rata Waktu Pengiriman (Hari)', fontsize=12)
    for index, value in enumerate(avg_shipping_time.values):
        plt.text(index, value + 0.5, f'{value:.1f}', ha='center')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    st.write("**Kesimpulan:** Lokasi pelanggan yang lebih jauh dari pusat distribusi cenderung memiliki waktu pengiriman yang lebih lama.")
