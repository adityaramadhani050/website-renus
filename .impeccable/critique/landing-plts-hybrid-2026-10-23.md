# Critique: prototypes/landing-plts-hybrid.html — 23 Okt 2026

⚠️ DEGRADED: single-context (sub-agent tidak dipakai di sesi ini). Assessment A (review visual) dilakukan sebelum membaca hasil detektor; Assessment B = `impeccable detect` render Chromium 1280×800 & 390×844.

Skor heuristik: 25/32 (Good) — H7 & H10 n/a (landing page).
Verdict spesifisitas: hero spesifik produk (lulus); 10 section setelah hero memakai template seragam (eyebrow kecil + H2 + grid kartu bulat ber-border) yang bisa dipakai kontraktor apa pun (gagal).

Isu prioritas:
1. [P1] Ritme seragam setelah hero: 9 section dengan pola dan padding sama, selang-seling putih/biru pucat → terasa "template". Fix: 2–3 section bernada berbeda (band navy penuh untuk angka, galeri foto full-bleed, section bertipografi besar). /impeccable layout, /impeccable bolder
2. [P1] Foto proyek asli terkecil kontribusinya: galeri di tengah, kartu solusi pakai foto sebagai latar redup. Fix: galeri full-bleed tepat setelah strip bukti; foto di kartu sistem. /impeccable layout
3. [P2] Angka besar (500+, 10 MWp+, 40.000+ kWh) kecil di strip & kartu → bukti terkuat tidak terasa. Fix: band angka besar. /impeccable bolder
4. [P2] Kartu dengan radius & border sama di semua tempat (sistem, paket, artikel, kontak, kalkulator) → hierarki datar. /impeccable polish
5. [P2] Biru muda #039cfc dengan teks putih 2,9:1 (keputusan pengguna) — masih satu-satunya kegagalan kontras nyata di detektor.

Detektor setelah perbaikan audit: low-contrast hanya tombol biru (7) + kartu solusi (false positive: foto tidak termuat di sandbox); overused-font (Plus Jakarta Sans, disengaja); pulsing-dot (titik hero, disengaja); border-accent strip HP (kode warna energi).
