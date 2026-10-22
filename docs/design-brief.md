# Design Brief — Redesain Total renergynusantara.com

Disepakati 22 Oktober 2026. Referensi gaya: hero situs Mersol (foto gelap layar penuh, headline besar rata kiri, satu warna aksen, header tipis transparan, bukti sosial di dasar hero).

Prototipe: `prototype/hero-animasi.html` (hero + animasi cara kerja).

## Keputusan

| Topik | Keputusan |
|---|---|
| Warna aksen | Tetap **biru Renus `#039CFC`** di atas dasar navy/hitam |
| Gambar hero | **Render/AI** bergaya referensi, dibuat pemilik situs memakai prompt di bawah |
| Headline | H1 label kecil "Kontraktor PLTS Surabaya & Jabodetabek" + headline besar "Listrik surya, siang sampai malam." |
| Bukti sosial di hero | Angka & sertifikasi: 14.375.000+ kWh/tahun · 5+ tahun · ISO 9001:2015 · Badan Usaha ESDM DJK |
| Animasi | Siklus otomatis Siang → Malam → PLN Padam + tombol pilihan, ilustrasi SVG |
| Nuansa setelah hero | Terang & lega (putih / abu sangat muda, ruang kosong lebar) |
| Font | **Plus Jakarta Sans** (400/500/600/700) |

> **Catatan aturan SEO no. 10** (CLAUDE.md: utamakan foto proyek asli, bukan gambar AI): pemilik situs memilih render/AI untuk hero. Konsekuensinya: alt text tidak boleh menyebut gambar sebagai proyek Renus, dan foto proyek asli tetap dipakai di galeri/portofolio.

## Token desain

| Token | Nilai | Pemakaian |
|---|---|---|
| `--rn-ink` | `#01141C` | latar hero, overlay |
| `--rn-navy` | `#00384F` | judul di latar terang, footer |
| `--rn-blue` | `#039CFC` | tombol utama, aliran listrik, aksen |
| `--rn-blue-hover` | `#0287DA` | hover tombol |
| `--rn-sky-light` | `#7CCBFF` | label H1 di atas latar gelap |
| `--rn-text` | `#12232D` | teks isi |
| `--rn-muted` | `#5B6B78` | teks sekunder |
| `--rn-line` | `#E3EAEF` | garis/batas |
| `--rn-bg-soft` | `#F5F8FA` | latar section selang-seling |
| `--rn-green` | `#22B07D` | indikator baterai |

Tipografi: display 44–96px / 600 / letter-spacing −0.035em / line-height 1.02; H2 32–52px / 600 / −0.03em; eyebrow 13px / 600 / huruf kapital / spasi 0.14em; isi 16–19px / 1.6.

Komponen: tombol pil (radius 999px), tombol utama biru isi putih, tombol kedua bergaris putih/biru tipis; kartu radius 28px dengan bayangan lembut.

## Hero

- Header Kadence **transparan** di homepage: logo putih kiri, menu tengah (Layanan, Produk, Proyek, Tentang Kami, Artikel, Hubungi Kami), pil kanan "● Konsultasi Gratis".
- Tinggi layar penuh (min. 640px). Overlay gradasi gelap dari kiri agar teks terbaca; subjek gambar di separuh kanan.
- Tombol: "Konsultasi Gratis" (utama) dan "Hitung Estimasi" (ke kalkulator).
- Baris angka di dasar hero dengan garis tipis di atasnya; di mobile menjadi 2×2 di bawah tombol.

## Animasi cara kerja PLTS hybrid

- Ilustrasi SVG ringan (tanpa library): panel surya → inverter → rumah, inverter ↔ baterai, PLN → inverter.
- Tiga keadaan, berganti otomatis tiap 6 detik (berhenti saat pengunjung memilih tab, hanya berjalan saat terlihat di layar, mati otomatis bila pengguna memilih *reduced motion*):
  - **Siang** — panel → rumah, sisa → baterai. Tidak ada aliran ke PLN (aturan SEO no. 6).
  - **Malam** — baterai → rumah, PLN siaga sebagai cadangan.
  - **PLN Padam** — jaringan putus (merah), baterai menjaga beban penting.
- Di WordPress dipasang sebagai satu blok Custom HTML.

## Prompt gambar hero (render/AI)

**Prompt (bahasa Inggris, hasil generator umumnya lebih baik):**

> Photorealistic architectural photograph, aerial three-quarter view from the front-left at about 30 degrees, of a modern two-storey tropical Indonesian house at blue hour (dusk). Dark grey standing-seam metal roof fully covered with black monocrystalline solar panels. Warm interior lights glowing through large glass windows, natural wood accents, a covered terrace. A wall-mounted hybrid inverter and lithium battery unit visible on the carport wall. Lush tropical garden with palm trees, frangipani and banana plants, surrounded by dense dark green tropical trees. The house sits in the right half of the frame; the left half is calm, dark foliage with little detail as negative space for text. Cinematic, moody deep navy and teal color grading with soft warm highlights, high dynamic range, sharp details, 16:9.

**Negative prompt / hindari:** people, text, logos, watermark, snow, pine trees, European cabin, distorted or melted solar panels, cartoon, oversaturated colors.

**Spesifikasi file:**
- Ukuran 2560×1440 px (minimal 1920×1080), rasio 16:9.
- Ekspor **WebP kualitas ±75, di bawah 350 KB** (shared hosting).
- Nama file: `plts-hybrid-rumah-tropis-senja.webp`.
- Alt text: "Ilustrasi rumah tropis dengan panel surya di atap saat senja".
- Opsional versi mobile 1080×1350 px dengan rumah di tengah.
- Pastikan atap & panel terlihat jelas dan bentuk panel lurus/rapi; ulangi generate bila panel terlihat bengkok.

## Rencana penerapan

1. Konfirmasi prototipe ini → revisi bila perlu.
2. Pemilik situs upload render hero ke Media Library.
3. Bangun ulang `blocks/homepage.html` dengan gaya baru (hero Cover block, animasi Custom HTML, section terang), lalu halaman draft untuk preview di WordPress.
4. Atur Kadence: font Plus Jakarta Sans (Customizer → Typography), header transparan untuk homepage, pil "Konsultasi Gratis" di header.
5. Lanjut ke halaman lain (Tentang Kami, Layanan, Produk, Proyek, Hubungi Kami, Artikel) memakai token & komponen yang sama.
