# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

### Permasalahan Bisnis
Namun Jaya Jaya Institut kini mengalami masalah tingginya angka dropout atau putus studi. Hal ini berdampak buruk terhadap reputasi institusi. Tujuan dari proyek ini adalah untuk membangun sistem prediktif menggunakan machine learning agar dapat mengidentifikasi siswa yang berpotensi dropout sejak dini. Dengan demikian, pihak institusi dapat memberikan perhatian dan intervensi khusus sebelum siswa memutuskan keluar dari institusi.

Objective: Memprediksi kemungkinan dropout seorang siswa berdasarkan data historis performa dan latar belakangnya.

### Cakupan Proyek
1. Menganalisis faktor penyebab dropout siswa.
2. Membuat model machine learning yang dapat digunakan untuk prediksi sederhana yang dapat di akses online.
3. Membangun dashboard menggunakan metabase untuk analisis penyebab terjadinya dropout

### Persiapan

Sumber data: [students_performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:
```
cd streamlit
python -m venv venv
venv\Scripts\activate
```

menginstall library yang diperlukan : 
```
pip install -r requirements.txt # install requirements.txt untuk aplikasi streamlit
```

menjalankan model menggunakan streamlit :
```
streamlit run app.py
```

## Credentials Metabase:
- Email: dev@hafizcaniago.my.id
- Password: root123

## Business Dashboard
![Dashboard Image](https://raw.githubusercontent.com/hafizcode02/bpds-student-performance/refs/heads/main/hafizcaniago-dashboard.png)

Dashboard yang dibuat merupakan salah satu solusi untuk mengatasi tingginya jumlah dropout pada Jaya Jaya Institute, disini saya menampilkan beberapa data yang memiliki korelasi terhadap dropout siswa seperti :
- Visualisasi Statistik Status Siswa
- Korelasi Dropout dengan Umur Siswa
- Korelasi Nilai Rata Rata untuk Setiap Semester terhadap Dropout Siswa

## Menjalankan Sistem Machine Learning

![Streamlit Image](https://raw.githubusercontent.com/hafizcode02/bpds-student-performance/refs/heads/main/hafizcaniago-streamlit.png)

*jika ingin menjalankan secara lokal di komputer*
```
streamlit run app.py
```
*jika ingin menjalankan langsung dengan mengunjungi website*
1. Untuk menjalankan sistem, silahkan kunjungi : [Link Streamlit on VPS](https://dropout-submission.hafigo.web.id/) | [Link Streamlit Community](https://hafigo-student-dropout.streamlit.app/)
2. maka akan tampil sperti gambar diatas, lalu silahkan sesuaikan inputan dengan siswa yang ingin diprediksi statusnya apakah termasuk dropout atau tidak
3. selanjutnya tekan prediksi maka akan tampil hasil prediksi beserta probabilitasnya dalam bentuk tabel.

## Conclusion
- Berdasarkan hasil analisis yang dilakukan dan dituangkan pada notebook, terdapat beberapa faktor yang paling mempengaruhi tingkat dropout siswa diantaranya adalah nilai akhir semester siswa, dimana siswa yang memiliki nilai yang rendah cenderung di-dropout
- Selanjutnya yang mempengaruhi dropout adalah biaya pendidikan sesuai dengan yang terbaru, ini cukup mempngaruhi karena jika tidak sesuai maka potensi dropout lebih tinggi jika biaya sesuai dengan biaya terbaru.
- Penerima beasiswa sangat mempengaruhi motivasi pelajar untuk menyelesaikan pendidikannya, tidak heran jika orang yang mendapatkan beasiswa akan berusaha sedini mungkin untuk terhindar dari dropout.

### Rekomendasi Action Items

1. Optimalisasi Dukungan Akademik
- **Pendampingan Proses Belajar**: Menyediakan program bimbingan belajar tambahan untuk siswa yang memiliki nilai rendah dan berisiko mengalami kesulitan akademik dan butuh perhatian khusus.
- **Pemberian Feedback yang Cepat**: Memberikan umpan balik langsung kepada siswa terkait performa mereka agar dapat memperbaiki nilai nya sebelum terlambat.

2. Peningkatan Akses Beasiswa
- **Program Beasiswa Baru**: Menyediakan lebih banyak peluang beasiswa, terutama untuk siswa dari latar belakang ekonomi yang kurang mampu.

3. Penyesuaian Biaya Pendidikan
- **Skema Pembayaran Fleksibel**: Memberikan opsi pembayaran cicilan atau pengurangan biaya bagi siswa yang menghadapi kesulitan ekonomi.
- **Subsidi Pendidikan**: Berkolaborasi dengan pihak ketiga untuk memberikan subsidi biaya pendidikan bagi siswa kurang mampu.
