import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('img', exist_ok=True)

# Set high-DPI style
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 0.8

# -------------------------------------------------------------
# 1. FIG 2.1: KERANGKA KONSEPTUAL KONVERGENSI HULU-HILIR (SI-KAPADAM)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

# Draw boxes
def draw_box(x, y, w, h, title, subtitle, color, edgecolor, icon_text=""):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.06",
                                 linewidth=1.5, edgecolor=edgecolor, facecolor=color)
    ax.add_patch(box)
    ax.text(x + w/2, y + h*0.68, title, ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0f172a')
    ax.text(x + w/2, y + h*0.35, subtitle, ha='center', va='center', fontsize=8, color='#475569', multialignment='center')

# Hulu
draw_box(0.05, 0.65, 0.25, 0.26, "1. SISI HULU (Pemicu)", "SiPongi KLHK & FIRMS\n• Hotspot Satelit MODIS/VIIRS\n• FDRS BMKG (Tingkat Bahaya)", "#ffe4e6", "#e11d48")

# Transmisi
draw_box(0.375, 0.65, 0.25, 0.26, "2. TRANSMISI ASMOSFER", "Stasiun BMKG Syamsudin Noor\n• Vektor Angin Tenggara\n• Model Dispersi Gaussian Plume", "#fef3c7", "#d97706")

# Hilir
draw_box(0.70, 0.65, 0.25, 0.26, "3. SISI HILIR (Dampak)", "IQAir & DLH Banjarmasin\n• Indeks AQI Real-Time\n• Konsentrasi PM2.5 Mikro-Polutan", "#e0f2fe", "#0284c7")

# Platform Pusat SI-KAPADAM
draw_box(0.20, 0.34, 0.60, 0.22, "PLATFORM GEOPORTAL SI-KAPADAM (ENGINE SPASIAL)", 
         "• Integrasi Spatial Buffer Peri-Urban (Radius 5–25 Km)\n• Validasi Pasang-Surut Kanal (Pushidrosal Trisakti) untuk Pompa Hisap BPK\n• Modul Crowdsourcing Partisipatif (VGI) Relawan Kebakaran Lapangan", 
         "#f1f5f9", "#3b82f6")

# Output Kebijakan & Komando
draw_box(0.05, 0.05, 0.26, 0.20, "Dinas Pendidikan (Disdik)", "DSS Penyesuaian Jam Masuk\nSekolah & Kebijakan PJJ Daring", "#e0e7ff", "#4f46e5")
draw_box(0.37, 0.05, 0.26, 0.20, "Dinas Kesehatan (Dinkes)", "Siaga Posko Oksigen Puskesmas\n& Pembagian Masker N95 Rentan", "#fce7f3", "#db2777")
draw_box(0.69, 0.05, 0.26, 0.20, "Armada BPK (BALAKAR 654)", "Mobilisasi Pompa ke Titik Api &\nNavigasi Saluran Pasang (>1.5m)", "#dcfce7", "#16a34a")

# Arrows
arrow_kw = dict(arrowstyle="->,head_width=0.4,head_length=0.6", color="#64748b", lw=1.5)
ax.annotate("", xy=(0.37, 0.78), xytext=(0.305, 0.78), arrowprops=arrow_kw)
ax.annotate("", xy=(0.695, 0.78), xytext=(0.63, 0.78), arrowprops=arrow_kw)

# From Top to Middle
ax.annotate("", xy=(0.35, 0.57), xytext=(0.20, 0.65), arrowprops=arrow_kw)
ax.annotate("", xy=(0.50, 0.57), xytext=(0.50, 0.65), arrowprops=arrow_kw)
ax.annotate("", xy=(0.65, 0.57), xytext=(0.80, 0.65), arrowprops=arrow_kw)

# From Middle to Bottom
ax.annotate("", xy=(0.18, 0.26), xytext=(0.35, 0.34), arrowprops=arrow_kw)
ax.annotate("", xy=(0.50, 0.26), xytext=(0.50, 0.34), arrowprops=arrow_kw)
ax.annotate("", xy=(0.82, 0.26), xytext=(0.65, 0.34), arrowprops=arrow_kw)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.title("Gambar 2.1 Kerangka Konseptual Konvergensi Hulu-Hilir Platform SI-KAPADAM", fontsize=11, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('img/fig_2_1_framework.png', dpi=300)
plt.close()

# -------------------------------------------------------------
# 2. FIG 4.1: KORELASI HOTSPOT SIPONGI & LONJAKAN PM2.5 IQAIR (2023-2025)
# -------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(9, 4.5), dpi=300)
ax1.set_facecolor('#ffffff')
fig.patch.set_facecolor('#ffffff')

months = ['Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November']
hotspots = [8, 24, 185, 412, 298, 45]  # Rata-rata hotspot ring perbatasan
pm25_levels = [28.4, 45.2, 118.6, 178.5, 142.0, 38.5] # Konsentrasi PM2.5 (ug/m3)

x = np.arange(len(months))
width = 0.42

# Bar for Hotspots
bars = ax1.bar(x - width/2, hotspots, width, label='Jumlah Hotspot SiPongi (Radius 25 Km)', color='#f43f5e', alpha=0.85, edgecolor='#be123c')
ax1.set_ylabel('Akumulasi Titik Panas (Hotspot)', color='#be123c', fontsize=9.5, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#be123c')
ax1.set_ylim(0, 500)
ax1.grid(axis='y', linestyle='--', alpha=0.3)

# Line for PM2.5
ax2 = ax1.twinx()
line = ax2.plot(x + width/2, pm25_levels, color='#0284c7', marker='o', linewidth=2.5, markersize=7, label='Konsentrasi Rata-rata PM2.5 IQAir (µg/m³)')
ax2.axhline(55, color='#d97706', linestyle=':', linewidth=1.5, label='Baku Mutu PP 22/2021 (55 µg/m³)')
ax2.set_ylabel('Konsentrasi PM2.5 (µg/m³)', color='#0284c7', fontsize=9.5, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='#0284c7')
ax2.set_ylim(0, 220)

# Set X ticks
ax1.set_xticks(x)
ax1.set_xticklabels(months, fontsize=9.5, fontweight='bold')
ax1.set_xlabel('Bulan Pemantauan (Fase Musim Kemarau)', fontsize=9.5, fontweight='bold', labelpad=8)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=8.5)

plt.title("Gambar 4.1 Korelasi Dinamika Titik Panas SiPongi terhadap Lonjakan Polutan PM2.5 di Banjarmasin", fontsize=10.5, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig('img/fig_4_1_hotspot_pm25_trend.png', dpi=300)
plt.close()

# -------------------------------------------------------------
# 3. FIG 4.2: FLUKTUASI PASANG SURUT AIR KANAL & EFISIENSI POMPA BPK
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4.2), dpi=300)
ax.set_facecolor('#ffffff')
fig.patch.set_facecolor('#ffffff')

hours = np.linspace(0, 24, 100)
# Tidal curve simulation in Barito/Martapura (Diurnal/Semi-diurnal mixture)
tide_height = 1.35 + 0.85 * np.sin((hours - 4) * np.pi / 7.5) + 0.25 * np.sin((hours - 10) * np.pi / 4)

ax.plot(hours, tide_height, color='#0891b2', linewidth=2.5, label='Elevasi Muka Air Saluran Rawa Pasut (m)')
ax.axhline(0.8, color='#dc2626', linestyle='--', linewidth=1.5, label='Ambang Batas Kritis Hisap Pompa Jinjing BPK (0.8 m)')

# Fill zones
ax.fill_between(hours, tide_height, 0.8, where=(tide_height >= 0.8), color='#22d3ee', alpha=0.25, label='Zona Air Cukup (Pompa Beroperasi Optimal)')
ax.fill_between(hours, tide_height, 0.8, where=(tide_height < 0.8), color='#f87171', alpha=0.3, label='Zona Kering / Surut Kritis (Risiko Hisap Lumpur)')

ax.set_xlabel('Waktu Operasional 24 Jam (WITA)', fontsize=9.5, fontweight='bold', labelpad=8)
ax.set_ylabel('Tinggi Muka Air di Saluran / Kanal (m)', fontsize=9.5, fontweight='bold')
ax.set_xlim(0, 24)
ax.set_ylim(0.2, 2.5)
ax.set_xticks(np.arange(0, 25, 2))
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=8.5)

plt.title("Gambar 4.2 Profil Pasang-Surut Saluran Drainase Rawa dan Jendela Waktu Efektif Pemadaman BPK", fontsize=10.5, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig('img/fig_4_2_tidal_water_routing.png', dpi=300)
plt.close()

print("All scientific charts generated successfully!")
