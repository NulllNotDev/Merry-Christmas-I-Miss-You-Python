# 🎵 Python Lyric Display — Merry Christmas I Miss You

Bot Python yang nampilin lirik lagu sinkron sama musik di terminal, dengan efek speed ramp di video hasil recordingnya.

---

## 📁 Struktur Folder

```
📁 projek/
├── lirik.py        ← script utama
└── 461376.mp4      ← file musik/video
```

---

## ⚙️ Requirements

- Python 3.x
- ffmpeg (sudah terinstall di PATH)

### Install ffmpeg (Windows)
```bash
winget install ffmpeg
```
Test:
```bash
ffmpeg -version
```

---

## ▶️ Cara Jalanin

```bash
cd C:\Users\ASUS\Downloads\projek
python lirik.py
```

---

## 🎵 Cara Ubah Timing Lirik

Buka `lirik.py`, edit bagian ini:

```python
lyrics = [
    (0.0,  ""),                              # detik ke-0, kosong dulu
    (3.0,  "✨ yeah, i miss you"),           # muncul di detik ke-3
    (6.5,  "🥀 you know it's true"),        # muncul di detik ke-6.5
    (10.8, "📞 so what if i call,"),
    ...
]
```

> Angka pertama = **detik berapa lirik muncul dari awal lagu**
> Ubah angkanya sampai pas sama musiknya

---

## 🎬 Cara Edit Speed Video (Alight Motion)

Setelah video direcord, import ke **Alight Motion** lalu atur speed di tiap bagian:

### Rangkuman Speed Ramp

| Timestamp | Speed | Keterangan |
|-----------|-------|------------|
| 0:00 — 0:09.09 | **0.50x** | Diperlambat di awal |
| 0:09.09 — 0:10.35 | **1.35x** | Naik cepat |
| 0:10.35 — 0:12.29 | **1.00x** | Kembali normal |
| 0:12.29 — 0:13.29 | **1.45x** | Naik lagi |
| 0:13.29 — 0:17.58 | **1.00x** | Kembali normal |
| 0:17.58 — selesai | **1.00x** | Default sampai akhir |

---

### ✨ Cara Set Speed Ramp dengan Keyframe di Alight Motion

Keyframe adalah fitur yang bikin perubahan speed terasa smooth — bukan langsung loncat, tapi naik/turun secara halus kayak efek kristal.

**Langkah-langkah:**

**1. Import video**
- Buka Alight Motion
- New Project → sesuaikan resolusi dan FPS
- Tap **+** → tambah video recording kamu

**2. Split video di titik timestamp**
- Geser playhead ke timestamp yang mau diubah (contoh: 9.09 detik)
- Tap video clip → pilih **Split**
- Ulangi di setiap titik perubahan speed:
  - 9.09 detik
  - 10.35 detik
  - 12.29 detik
  - 13.29 detik
  - 17.58 detik

**3. Set speed tiap segment**
- Tap segment pertama (0 — 9.09 detik)
- Tap ikon **⏱ Speed** atau masuk ke properties clip
- Set speed ke **0.50x**
- Ulangi untuk segment berikutnya sesuai tabel di atas

**4. Tambah Keyframe buat smooth transition (efek kristal)**
- Tap clip yang mau dikasih efek smooth
- Tap ikon **◆ Keyframe** (biasanya di toolbar atas)
- Geser playhead ke **awal transisi** → set speed awal
- Geser playhead ke **akhir transisi** → set speed tujuan
- Alight Motion otomatis bikin perubahan speed yang smooth di antara dua keyframe itu

> 💡 Makin jauh jarak antar keyframe = transisi makin smooth/halus
> Makin dekat = transisi lebih cepat/dramatis

**5. Preview & Export**
- Tap ▶ buat preview
- Kalau udah pas → **Export** → pilih kualitas

---

## 🛠️ Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Musik tidak bunyi | Pastiin ffmpeg terinstall & file mp4 ada di folder yang sama |
| Lirik tidak sinkron | Edit timestamp di `lyrics = [...]` di `lirik.py` |
| CMD ada log ffmpeg | Ketik `cls` sebelum record |
| Error `python not found` | Pastiin Python sudah terinstall dan ada di PATH |

---

## 📝 Cara Ubah Lirik

Edit bagian `lyrics` di `lirik.py`:

```python
lyrics = [
    (0.0,  ""),
    (3.0,  "✨ teks lirik pertama"),
    (6.5,  "🥀 teks lirik kedua"),
    # tambah terus sesuai lagu
    (53.6, ""),   # akhir lagu, kosongkan
]
```

## 📝 Wajib Baca
Kalau mau pake buat content, pastikan credit author dan tag akun tt creator, dan masuk kan user github creator di deskripsi video yaahh
# tiktok :
# @nullthemanwhocantbemoved
# @marz_official11

#github :
# @NulllNotDev

Bisa pake emoji bebas di depan tiap lirik buat estetik! ✨

---

*Made with Python + ffmpeg + Alight Motion*
