# Halaman Artikel (`/artikel/`, ID 10131) — Gutenberg

- 24 Okt 2026: halaman ternyata **kosong sejak 2025** (`_elementor_edit_mode=builder` tanpa `_elementor_data`, konten kosong) → tampil putih.
- Dibangun ulang dengan `artikel.blocks.html`: wrapper `.rn` (gaya dari Additional CSS homepage), H1 "Panduan memilih dan memasang PLTS.", Query Loop 12 artikel/halaman (featured image 16:10, tanggal, judul, ringkasan) + paginasi.
- `_elementor_edit_mode` dihapus. Template `_wp_page_template` tetap `elementor_header_footer` (diproteksi; ganti ke default Kadence secara manual bila Elementor dinonaktifkan).
- Grid memakai class `.posts` yang sama dengan section Artikel homepage; gaya blok lain lewat atribut blok (tanpa CSS tambahan).
- Deploy ulang: `wp_update_page` id 10131 dengan isi `artikel.blocks.html`.
- Belum: meta description Yoast untuk /artikel/ masih kosong.
