# SI-KAPADAM: Sistem Geoinformatika Komando Armada Pemadam dan Pantau Asap Lahan Gambut Banjarmasin

[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](https://opensource.org/licenses/MIT)
[![WebGIS](https://img.shields.io/badge/WebGIS-Leaflet.js-rose.svg)](https://leafletjs.com/)
[![TailwindCSS](https://img.shields.io/badge/UI-TailwindCSS_v3-sky.svg)](https://tailwindcss.com/)
[![Target](https://img.shields.io/badge/Bappedalitbang-LKTI_2026-amber.svg)](https://bappedalitbang.banjarmasinkota.go.id/)

> **Karya Tulis Ilmiah (LKTI) Inovasi Daerah Bappedalitbang Kota Banjarmasin Tahun 2026**  
> **Sub-Tema (h):** *Kesiapsiagaan, Pengurangan Risiko, Mitigasi, dan Pemulihan Bencana*  
> **Judul Lengkap:** *"SI-KAPADAM: Integrasi Data Geospasial SiPongi KLHK dan Monitoring Real-Time PM2.5 IQAir Terkoneksi Saluran Pasang-Surut Rawa dalam Respon Cepat Karhutla Peri-Urban Kota Banjarmasin"*

---

## 🌐 Demo WebGIS Live
Akses purwarupa aplikasi WebGIS interaktif secara langsung melalui:  
🔗 **[https://nouranisa.github.io/SI-KAPADAM/](https://nouranisa.github.io/SI-KAPADAM/)**

---

## 📌 Latar Belakang & Urgensi

Kota Banjarmasin memiliki karakteristik geografis deltaik lahan basah pasang-surut yang rentan terhadap dampak kabut asap lintas batas (*transboundary smoke haze*) akibat kebakaran hutan dan lahan (karhutla) di wilayah peri-urban penyangga (Kertak Hanyar, Gambut, Lingkar Selatan, Liang Anggang). Bencana kabut asap tahunan ini melumpuhkan aktivitas belajar-mengajar di sekolah, penerbangan di Bandara Internasional Syamsudin Noor, serta memicu lonjakan kasus Infeksi Saluran Pernapasan Akut (ISPA).

Meskipun Kota Banjarmasin memiliki potensi sosial luar biasa berupa **lebih dari 600 unit Barisan Pemadam Kebakaran (BPK) swasta/relawan** (terpadat di Indonesia), upaya pemadaman karhutla perbatasan kerap terkendala oleh:
1. **Pemisahan Data (*Data Silo*):** Data titik api satelit (SiPongi KLHK) dan data dampak polusi udara (IQAir / DLH) berjalan sendiri-sendiri tanpa jembatan korelasi prediktif.
2. **Keterbatasan Pasokan Air Pompa:** Kanal-kanal drainase rawa dipengaruhi oleh dinamika pasang-surut (*tidal fluctuation*). Saat air surut, kanal mengering sehingga pompa pemadam jinjing milik relawan BPK tidak dapat menyedot air.
3. **Respon Kebijakan Reaktif:** Kebijakan penyesuaian jam sekolah (PJJ) atau pembagian masker sering terlambat dikeluarkan karena ketiadaan sistem pendukung keputusan (*Decision Support System* / DSS) otomatis.

---

## 💡 Solusi Inovasi: Platform SI-KAPADAM

**SI-KAPADAM** hadir mengintegrasikan pendekatan **hulu-ke-hilir (*end-to-end*)**:
* **Sisi Hulu (Deteksi Dini Api):** Mengambil data *hotspot* satelit (Terra/Aqua MODIS dan SNPP/NOAA-20 VIIRS) dari sistem SiPongi KLHK dalam radius *buffer* 25 km dari batas Kota Banjarmasin.
* **Sisi Hilir (Dampak Kesehatan):** Memantau konsentrasi partikulat halus $PM_{2.5}$ dan Indeks Kualitas Udara (AQI) secara *real-time* berbasis stasiun pemantauan IQAir dan DLH Kota Banjarmasin.
* **Sisi Operasional Hidrologi:** Menghubungkan jaringan kanal irigasi rawa (Dinas PUPR / BIG) dengan jadwal pasang-surut harian (Pushidrosal Pelabuhan Trisakti) untuk memandu armada pemadam ke sumber air aktif.
* **Partisipasi Komunitas (VGI):** Memberdayakan jejaring induk **BALAKAR 654 Banjarmasin** melalui pelaporan cepat terverifikasi lapangan (*Volunteered Geographic Information*).
* **Automated Decision Support System (DSS):** Menghasilkan rekomendasi kebijakan instan bagi Dinas Pendidikan (penyesuaian jam sekolah), Dinas Kesehatan (siaga masker & faskes), dan BPBD/DPKP (level siaga darurat).

---

## 🏛️ Arsitektur Sistem

```
┌────────────────────────────────────────────────────────────────────────┐
│                        SUMBER DATA RESMI & VALID                       │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ 1. SiPongi KLHK   │ 2. IQAir & DLH    │ 3. Pushidrosal & BMKG          │
│    (Hotspot & FRP)│    (PM2.5 & AQI)  │    (Pasut & Arah Angin)        │
└─────────┬─────────┴─────────┬─────────┴───────────────┬────────────────┘
          │                   │                         │
          ▼                   ▼                         ▼
┌────────────────────────────────────────────────────────────────────────┐
│                 ENGINE SPASIAL & ANALISIS PREDIKTIF                    │
│   • Buffer Peri-Urban (Radius 5–25 Km Ring Luar Banjarmasin)           │
│   • Gaussian Plume Smoke Dispersion Modeling (BMKG Wind Vector)        │
│   • Water Availability Routing (Tidal Elevation Validation)            │
└─────────────────────────────────┬──────────────────────────────────────┘
                                  │
                                  ▼
┌────────────────────────────────────────────────────────────────────────┐
│                 DASHBOARD GEOPORTAL SI-KAPADAM                         │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ Peta WebGIS Live  │ Komando BPK 654   │ DSS Kebijakan Pemkot           │
│ (Leaflet & Carto) │ (Navigasi Air)    │ (Disdik, Dinkes, BPBD)         │
└───────────────────┴───────────────────┴────────────────────────────────┘
```

---

## 🛠️ Tumpukan Teknologi (*Tech Stack*)

* **Frontend & Interaktivitas:** HTML5 Semantik, Tailwind CSS v3, JavaScript Modern (ES6+).
* **Pemetaan Geospasial:** Leaflet.js, CartoDB Dark Matter Basemap, GeoJSON Layers.
* **Visualisasi Grafis:** Chart.js, Font Awesome 6 Icons, Google Fonts (Inter & Poppins).
* **Deployment:** GitHub Pages (SSL Terenkripsi & Responsif Seluler).

---

## 👥 Pengembang & Afiliasi
* **Institusi:** Program Studi Sistem Informasi, Universitas Sari Mulia (UNISM) Banjarmasin.
* **Peruntukan:** Naskah dan Purwarupa Lomba Karya Tulis Ilmiah Bappedalitbang Kota Banjarmasin Tahun 2026.
