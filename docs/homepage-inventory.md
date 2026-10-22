# Inventaris Konten Homepage (ID 3280)

Dibaca dari Elementor via Royal MCP pada 22 Oktober 2026 (read-only, belum ada perubahan).
Judul post: "Kontraktor PLTS Terpercaya | Jasa Pemasangan PLTS" (title Yoast terpisah, jangan diubah).

Kolom **Masalah** menandai hal yang wajib dibetulkan saat migrasi (merujuk ke nomor aturan SEO di `CLAUDE.md`).

---

## 1. Hero (section `118bce00`)

- Background: slideshow 7 foto (Ken Burns), overlay `#011B26`.
  - 4747 `WhatsApp-Image-2024-09-02-at-09.35.08-3-scaled.jpeg`
  - 4743 `WhatsApp-Image-2024-09-02-at-09.35.08-2-scaled.jpeg`
  - 4739 `WhatsApp-Image-2024-09-02-at-09.35.08-scaled.jpeg`
  - 3289 `DJI_0441-2-scaled.jpg`
  - 3292 `DJI_0105-2-scaled.jpg`
  - 3831 `20230724-DJI_0706-scaled.jpg`
  - 3835 `20230507-DJI_0479-scaled.jpg`
- H1 (`4120589`, elementskit-heading): **"Renewable Energy Solutions"**, 70px italic putih.
- H3 (`25aa8cd3`): "Menghadirkan Solusi Pembangkit Listrik Tenaga Surya (PLTS) Terdepan untuk Rumah dan Industri"

**Masalah:** H1 bahasa Inggris tanpa kata kunci (aturan 3). Ganti dengan H1 "Kontraktor PLTS Surabaya & Jabodetabek". Slideshow diganti satu gambar Cover (lebih ringan); usul: 3289 atau 3831.

## 2. Counter + "Mengapa harus pasang PLTS?" (section `5a151b98`)

- Label atas: "Telah berkontribusi menghasilkan"
- Counter (`29dd1663`, premium-counter): end value **14375**, separator ".", suffix **"K+"**, ikon ekiticons energy-saving.
- Label bawah: "kWh energi bersih tiap tahunnya"
- H?: "Mengapa harus pasang PLTS?"
- Teks: "Pembangkit Listrik Tenaga Surya (PLTS) di rumah dan industri memberikan manfaat ekonomis, lingkungan, dan keberlanjutan energi. Energi surya dapat mengurangi biaya listrik, mengurangi emisi karbon, dan meningkatkan kemandirian energi. Oleh karena itu Investasi awal dapat menghasilkan pengembalian jangka panjang dan memberikan citra berkelanjutan bagi bisnis."

**Masalah:** angka hanya dirender JS (aturan 4). Tulis statis: **"14.375K+ kWh"**. Catatan: "14.375K" = ±14,4 juta kWh/tahun — perlu konfirmasi apakah angka ini benar atau maksudnya 14.375 kWh.

## 3. Tentang Kami (section `32d768e1`)

- Eyebrow: "tentang kami"
- Heading: "Energi Surya untuk Keberlanjutan Dunia"
- Teks: "Kami bergerak dalam bidang energi, mekanikal dan elektrikal, khususnya yang berkaitan dengan sistem teknologi alternatif dan energi terbarukan. Kami juga telah bersertifikat badan usaha dari ESDM DJK dan telah bersertifikat ISO."
- Tombol "Selengkapnya" → `https://renergynusantara.com/tentang-kami/`
- Gambar: 3529 `WhatsApp-Image-2023-04-03-at-00.22.45.jpeg` (alt kosong)

**Masalah:** alt kosong (aturan 10). Sebut "ISO 9001:2015" secara spesifik.

## 4. Bisnis Kami (sections `2479db6`, `1cf5dd8a`)

- Eyebrow: "Bisnis Kami"
- Heading: "Tingkatkan Efisiensi Energi dan Hemat Biaya Listrik Anda"

| Kartu | Gambar | Deskripsi | Link sekarang | Link wajib (aturan 5) |
|---|---|---|---|---|
| Residensial | 3180 `DJI_0034-scaled.jpg` | Gunakan energi surya untuk kebutuhan sehari-hari di rumah Anda dan nikmati manfaat energi terbarukan yang ramah lingkungan dan hemat biaya listrik. | **tidak ada** | `/plts-hybrid/` |
| Komersial | 3289 `DJI_0441-2-scaled.jpg` | Solusi hemat energi dan ramah lingkungan untuk bisnis atau instansi Anda serta dapat meningkatkan citra sebagai perusahaan atau instansi yang peduli terhadap lingkungan. | **tidak ada** | `/pasang-plts-untuk-bisnis/` |
| Industrial | 4810 `DJI_0017-scaled.jpg` | Optimalkan operasional perusahaan dengan energi surya tidak hanya mengurangi beban biaya listrik secara signifikan, tetapi juga memberikan keandalan pasokan daya yang tinggi. | **tidak ada** | `/plts-industri-manufaktur/` |

Tombol "Selengkapnya" ada di ketiga kartu tapi tanpa URL. Semua alt kosong.

## 5. Solusi Kami — "Smart Solar Power System" (section `201e6ed7`)

| Kartu | Ikon (SVG) | Deskripsi | Link |
|---|---|---|---|
| PLTS On-Grid | 3939 `icon-plts-01.svg` | "Sistem terkoneksi ke jaringan listrik utama, mengalirkan listrik langsung dari panel surya ke jaringan listrik. **Energi berlebih atau kekurangan dapat disalurkan kembali ke jaringan listrik.** Sehingga sistem ini tidak memerlukan penyimpanan energi." | `/plts-on-grid/` |
| PLTS Off-Grid | 3946 `…-02-1.svg` | "Sistem ini bekerja secara independen tanpa ketergantungan pada listrik utama. Energi dari panel surya dapat digunakan langsung atau disimpan dalam baterai untuk digunakan ketika sinar matahari tidak mencukupi atau pada malam hari." | `/plts-off-grid/` |
| PLTS Hybrid | 3948 `…-03-1.svg` | "Sistem ini menggunakan energi surya secara langsung. Kelebihan listrik yang dihasilkan disimpan dalam baterai, yang dapat menyediakan daya tambahan jika energi matahari tidak mencukupi, atau mengambil listrik dari jaringan jika diperlukan." | `/plts-hybrid` (tanpa slash akhir) |

**Masalah:**
- Deskripsi On-Grid **melanggar aturan 6** (menyiratkan ekspor kelebihan listrik ke PLN). Wajib ditulis ulang.
- Fokus redesain = hybrid → urutan diusulkan: Hybrid (ditonjolkan) → Off-Grid → On-Grid.
- Cek apakah `/plts-on-grid/` ada atau sudah di-redirect (yang tercatat di CLAUDE.md adalah `/biaya-plts-on-grid/`).

## 6. Manfaat PLTS di Rumah (section `b8c1ac`)

- Kolom kiri: kartu dekoratif dengan background 3324 `DJI_0444-3-768x768.jpg`
- Eyebrow: "dapatkan manfaat"; Heading: "Penggunaan PLTS di Rumah Anda!"
- Intro: "Dapatkan manfaat luar biasa menggunakan energi bersih di rumah anda:"
- Daftar:
  - Energi bersih yang tidak terbatas
  - Hemat biaya listrik
  - Bebas dari pemadaman listrik
  - Mengurangi emisi karbon
  - Meningkatkan nilai properti
  - Kesempatan mendapat insetif pemerintah *(typo: "insentif")*
  - Memberikan edukasi untuk lingkungan sekitar

**Catatan:** "Bebas dari pemadaman listrik" hanya benar untuk hybrid/off-grid (on-grid mati saat PLN padam) — perlu diberi konteks.

## 7. Kalkulator PLTS (section `ded9e16`, widget HTML `08c4f81`)

~25 KB HTML+CSS+JS mandiri dalam `<div class="rn-calc">`. Alur 4 langkah: Tipe Properti → Konsumsi Daya → Data Kontak → Hasil Estimasi. Tidak mengirim data ke server; hasil berupa tautan WhatsApp (Jabodetabek → 6281412250644, selain itu → 6285385558025) dan mailto `sales@renergynusantara.com`.

Asumsi di kode: tarif PLN Rp 1.700/kWh; harga per kWp Rp 15/17/19 jt (residensial/komersial/industrial) × faktor sistem (hybrid 1,0 · off-grid 1,3 · on-grid 0,7); panel 500 Wp; 4 jam matahari puncak.

**Masalah / keputusan:**
- Hasil menampilkan **"Estimasi Investasi"** (termasuk pemasangan) — bertentangan dengan larangan menampilkan kisaran biaya pemasangan? **Perlu keputusan.**
- Penghematan dihitung dari produksi penuh × tarif; untuk on-grid ini bisa melebihi konsumsi (secara implisit menghitung kelebihan ekspor) — sebaiknya dibatasi maksimal sebesar tagihan (`min(produksi, konsumsi)`), sesuai aturan 6.
- Nama pengguna disisipkan ke `innerHTML` tanpa escape (hanya berdampak ke pengguna itu sendiri, tapi mudah diperbaiki).
- Gunakan blok Custom HTML; `<script>` hanya tersimpan bila akun MCP punya kapabilitas `unfiltered_html` (Administrator). Verifikasi setelah simpan ke staging.
- Typo: "lokasimi" → "lokasimu".
- Sumber asli disalin ke repo saat tahap build (`blocks/kalkulator-plts.html`).

## 8. Mengapa Memilih Renus (section `273c80ff`)

- Eyebrow: "Mengapa memilih Renus?"; Heading: "Lebih dari 5 Tahun berpengalaman di bidangnya"
- Kartu:
  - **Tim Ahli** — Berpengalaman dan bersertifikat, memastikan seluruh perhitungan tidak hanya terfokus pada aspek teknis tetapi juga aspek ekonomi.
  - **Komponen Terbaik** — Menggunakan komponen dari brand premium dengan kualitas terbaik yang memiliki perkiraan umur pemakaian hingga 15 tahun. (ikon 3897)
  - **Dukungan 24/7** — Konsultasi gratis mengenai pengadaan peralatan dan komponen tenaga surya, atau hanya jasa instalasi tenaga surya.
  - **Bersertifikat ISO** — Sertifikasi ISO menandakan komitmen terhadap keunggulan dan kualitas di seluruh aspek operasional. (ikon 3896 `iso-2-1.svg`)
- Gambar: 3682 `IMG_20230508_172438-scaled.jpg` (alt kosong)

**Usulan:** "Bersertifikat ISO" → "ISO 9001:2015 & Badan Usaha ESDM DJK".

## 9. Proyek Kami (sections `1a0b9ecd`, `3202f63`)

- Eyebrow: "portofolio"; Heading: "Proyek Kami"; tombol "Lihat Lainnya" → `/proyek/`
- Galeri (premium-img-gallery, masonry 3 kolom, filter kategori nonaktif):
  - 4743 `WhatsApp-Image-2024-09-02-at-09.35.08-2-scaled.jpeg` (Residensial)
  - 3289 `DJI_0441-2-scaled.jpg` (Komersial & Industrial)
  - 3292 `DJI_0105-2-scaled.jpg` (Komersial & Industrial)
  - 3487 `JIIPe-e1680162481413.jpg` (Komersial & Industrial)
  - 4129 `Screen-Shot-2024-01-10-at-16.21.08.png` (Komersial & Industrial)
  - 3180 `DJI_0034-scaled.jpg` (Residensial)

**Masalah:** semua alt kosong; nama file tidak deskriptif (aturan 10). Screenshot PNG (4129) sebaiknya diganti foto asli.

## 10. Klien Kami (sections `d734086`, `b91e78b`)

Dua carousel × 7 logo (tanpa autoplay, tanpa navigasi — praktis statis):

- Baris 1: 4063, 4060, 4061, 4062, 4064 (`Untitled-3-01-*.png`), 3796 `JATIM-1-…png`, 4073 `Untitled-3-01-9.png`
- Baris 2: 3856 `Logo_PU_RGB-scaled.jpg`, 4072, 4065 (`Untitled-3-01-*.png`), 3814 `lambang-its-png-v2.png`, 4066 `Untitled-3-01-6.png`, 3784 `Logo-Biru-Muda.png`, 4067 `Untitled-3-01-7.png`

**Masalah:** 11 dari 14 file bernama `Untitled-3-01-*`; perlu identifikasi nama klien per logo untuk alt text (WIKA, Medco, PUPR, ITS, Perpustakaan Jatim, dll.).

## 11. Artikel Terkini (section `7442f822`)

- Eyebrow: "Blog & artikel"; Heading: "Artikel Terkini"
- Tombol "Selengkapnya" → **`www.instagram.com/renergynusantara`** (tanpa https — juga link rusak relatif)
- Slider prime-slider-fiestar: 10 post terbaru, hanya yang berfeatured image, 3 kolom.

**Masalah:** tombol wajib → `/artikel/` (aturan 5). Ganti slider dengan blok Query Loop (3–6 post terbaru).

## 12. Popup "Alokasi Kuota Terbatas" (section `f5a099b`, widget HTML `7b5ff5b`)

Bukan Elementor Pro — ini HTML+JS kustom: overlay layar penuh yang **otomatis muncul 1,5 detik setelah halaman dibuka, di setiap kunjungan**. Isi: badge "Alokasi Kuota Terbatas", headline "Wujudkan Kemandirian Energi & Pangkas Tagihan Listrik Rumah Anda", 3 benefit (konsultasi & studi kelayakan gratis, simulasi ROI, survei lokasi gratis), CTA WhatsApp 6281412250644, link Instagram/Facebook/TikTok.

**Usulan:** ganti dengan CTA WhatsApp sticky (tidak menutupi konten). Popup layar penuh otomatis di mobile termasuk "intrusive interstitial" yang bisa merugikan peringkat Google. Jika tetap ingin popup: tampilkan sekali per sesi (sessionStorage) dan setelah scroll, bukan saat load.

---

## Ringkasan pelanggaran aturan SEO pada homepage saat ini

| Aturan | Status |
|---|---|
| 3. Tepat satu H1 berkata kunci | ❌ H1 = "Renewable Energy Solutions" |
| 4. Angka counter tertulis di HTML | ❌ hanya JS |
| 5. Kartu → /plts-hybrid/, /pasang-plts-untuk-bisnis/, /plts-industri-manufaktur/; Artikel → /artikel/ | ❌ kartu tanpa link; Artikel → Instagram |
| 6. On-Grid tanpa janji ekspor | ❌ "Energi berlebih … disalurkan kembali ke jaringan" |
| 10. Alt text deskriptif | ❌ semua gambar alt kosong |

## Pertanyaan untuk pemilik situs

1. Counter "14.375K+ kWh/tahun" — angka benar (±14,4 GWh) atau maksudnya 14.375 kWh?
2. Kalkulator: tetap tampilkan "Estimasi Investasi", atau hapus/ganti dengan harga paket katalog (material) saja?
3. Popup: ganti dengan CTA WhatsApp sticky, atau pertahankan dengan frekuensi dibatasi?
4. Nama klien untuk tiap logo `Untitled-3-01-*`.
