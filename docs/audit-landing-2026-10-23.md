# Audit `prototypes/landing-plts-hybrid.html` — 23 Okt 2026

Alat: `impeccable audit` + detektor `impeccable detect` (render Chromium 1280×800 & 390×844, dan scan sumber), ditambah cek Playwright: overflow 320/390/768 px, target sentuh, urutan heading, Tab keyboard, teks 200%.

Catatan lingkungan: gambar dari renergynusantara.com tidak bisa dimuat di sandbox audit, jadi temuan kontras pada kartu Solusi (teks putih di atas foto) adalah **false positive**: di situs asli teks itu berada di atas foto + gradasi gelap.

## Skor

| # | Dimensi | Skor | Temuan utama |
|---|---|---|---|
| 1 | Aksesibilitas | 2/4 | Teks putih di tombol biru 2,9:1; menu di atas langit terang 2,7–3,5:1 |
| 2 | Performa | 3/4 | Foto hero baru dimuat lewat JavaScript (LCP lambat) |
| 3 | Theming | 3/4 | Token rapi; sisa warna literal (border `#d5e4ea`, putih transparan) |
| 4 | Responsif | 3/4 | Tanpa scroll samping di 320 px; target sentuh < 44 px |
| 5 | Integritas implementasi | 3/4 | Sistem koheren & spesifik subjek; temuan detektor kecil |
| **Total** | | **14/20** | **Good** |

**Verdict integritas: lulus.** Halaman mengikuti `DESIGN.md` (token, satu keluarga font, warna energi bermakna), hero spesifik untuk produk (jalur energi menempel ke instalasi di foto), satu H1, tidak ada konten pengisi.

## Temuan

### P1 — perbaiki sebelum rilis
1. **Teks putih di tombol biru `#039cfc` = 2,9:1** (WCAG 1.4.3, butuh 4,5:1). Lokasi: tombol WhatsApp hero, pil mode aktif, tombol kontak Jabodetabek, tombol & badge kalkulator. Ini keputusan pengguna 23 Okt; opsi aman: latar tombol `#0277c0` (4,8:1) dengan teks putih tetap. → `/impeccable polish`
2. **Foto hero tidak punya `src`** — semua `<img>` di `.stage` hanya `data-srcset` yang diisi JS. Dampak: LCP tertunda sampai JS jalan; tanpa JS hero kosong; crawler bisa tidak melihat gambar. Rekomendasi: beri foto mode awal `src`/`srcset` asli + `fetchpriority="high"`, sisanya tetap lazy. → `/impeccable optimize`
3. **Menu header di atas langit terang** (mode Siang/Mendung): "Artikel", "Tentang Kami", "Hubungi Kami" 2,7–3,5:1. Rekomendasi: perkuat gradasi gelap di 120 px teratas hero atau beri latar navy transparan pada header. → `/impeccable polish`
4. **Gambar media library ukuran penuh** (`*-scaled.jpg` 2560 px; logo UHT 2,8 MB) dipakai di kartu 4:3 dan galeri. Saat migrasi pakai ukuran WordPress (`medium_large`/`large`) + `srcset`. → `/impeccable optimize`

### P2 — perbaiki di putaran berikutnya
5. **Eyebrow & tautan biru di section biru pucat**: `#0277c0` di atas `#e1f0f5` = 4,1:1 (Solusi, Kalkulator, Proses, Artikel). Pakai navy `#00384f` atau biru lebih gelap di section `.soft`. → `/impeccable polish`
6. **Target sentuh < 44 px**: pil mode 32 px, tautan "Tanya paket" 23 px, tautan "Semua …" 27 px, baris FAQ 27 px (WCAG 2.5.8 minimal 24 px; rekomendasi 44 px). → `/impeccable adapt`
7. **Teks kecil**: label strip angka HP 9,9 px; catatan "Angka ilustrasi…" 3,2:1. Naikkan ke ≥ 11–12 px dan opasitas teks. → `/impeccable typeset`
8. **Reduced motion menghapus arah aliran**: aturan global mematikan semua animasi, jadi denyut yang menunjukkan arah energi hilang tanpa pengganti. Tambahkan panah statis di ujung jalur untuk mode ini. → `/impeccable animate`

### P3 — polish
9. Cincin berdenyut di setiap titik aktif (detektor: *pulsing dot*); cukup di titik yang sedang mengalirkan energi.
10. `fitTags()` membaca layout setiap frame selama animasi Malam (7 detik); cukup dipanggil saat teks label berubah.
11. Tidak ada tautan "Lewati ke konten" untuk pengguna keyboard.

### Temuan detektor yang tidak ditindaklanjuti
- **Overused font (Plus Jakarta Sans)**: pilihan sengaja di `DESIGN.md` (via `ui-ux-pro-max`, buatan desainer Indonesia). Brief menang.
- **Border-top aksen pada kartu strip angka HP**: warna atas = kode warna energi (bermakna), bukan dekorasi.
- **Repeating stripes**: garis putus-putus penghubung langkah Proses (fungsional) dan placeholder di versi preview.
- **Tight leading H1 (1,06)**: wajar untuk judul display.

## Yang sudah baik
- Tepat satu H1, urutan heading H1→H2→H3 rapi, landmark `header`/`nav`/`main`/`footer`.
- Tombol mode memakai `<button>` + `aria-pressed`; deskripsi kondisi hero dibacakan lewat region `aria-live`.
- Semua input kalkulator punya `<label>`, error di dekat field, nama pengguna di-escape.
- Fokus keyboard terlihat (outline 3 px) dan urutan Tab logis.
- Tidak ada scroll horizontal di 320, 390, 768 px; teks 200% tetap muat.
- Foto hero WebP 26–300 KB, mode lain dimuat setelah halaman tampil; gambar di bawah lipatan `loading="lazy"`.

## Urutan tindakan
1. [P1] `/impeccable optimize` — `src` + `fetchpriority` foto hero; ukuran gambar WordPress saat migrasi.
2. [P1] `/impeccable polish` — kontras tombol biru, menu di atas langit, eyebrow di section pucat.
3. [P2] `/impeccable adapt` — target sentuh pil mode & tautan.
4. [P2] `/impeccable typeset` — teks strip angka HP & catatan ilustrasi.
5. [P2] `/impeccable animate` — panah statis untuk reduced motion.
6. `/impeccable polish` — pass akhir.
