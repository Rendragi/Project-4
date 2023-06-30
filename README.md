Project 4 - Bootcamp Data Engineer Batch 13 
Digital Skola

STEP 1: BUAT DATA KONEKSI DI FILE CONFIG_JSON

STEP 2: BUAT INSTALASI - INSTALASI YANG DIPERLUKAN DI FILE requirements.txt, 
LALU JALANKAN DENGAN MENULIS "pip install -r requirements.txt" PADA TERMINAL LALU ENTER

STEP 3: BUAT SCRIPT UNTUK MELAKUKAN KONEKSI KE POSTGRES DAN HADOOP
DI FILE connection.py

STEP 4: CONNECT KE POSTGRES DAN HADOOP 

STEP 5: UPLOAD FILE DARI POSTGRES KE DWH HADOOP DENGAN NAMA FILE DIM_ORDERS_{NAMA}

UPLOAD KE HADOOP BERHASIL
![img1](IMG\Screenshot(84).png)

STEP 6: BUAT SCRIPT TRANSFORM DATA DENGAN MAPREDUCE DI FILE mapReduce.py
SCRIPT MAPREDUCE INI UNTUK MENGHITUNG JUMLAH ORDER PER BULANNYA

STEP 7: BUAT DATA MART DENGAN MAPREDUCE DARI DATA DWH HADOOP
OUTPUT DATA MART DI LOCAL
![img1](IMG\Screenshot(85).png)

TAMBAHAN: UPLOAD DATA MART DARI LOCAL KE POSTGRES DENGAN NAMA FILE total_orders_based_on_month DENGAN MENJALANKAN FILE insert_to_postgres.py
![img1](IMG\Screenshot(87).png)







 




