# Tentang Kami (`/tentang-kami/`, ID 44)

- Sumber lama: `elementor-source.json` (data Elementor sebelum migrasi, untuk rujukan & rollback).
- Isi baru: `tentang-kami.blocks.html`, dihasilkan `python3 ../pages/build_pages.py tentang-kami`.
- Copy dirapikan (skill copy-editing): fakta diperbarui sesuai CLAUDE.md — 6+ tahun (lama "5 tahun"), ISO 45001:2018 (lama tertulis 2015), ditambah ISO 37001:2025, "Dukungan 24/7" → "Konsultasi gratis" (klaim 24/7 tidak terverifikasi).
- Gambar memakai ukuran `large`/`medium_large`; sertifikat SBU (PNG 4,7 MB asli) pakai 768 px (830 KB) — kandidat konversi WebP.
- Hero: foto penuh (`page-hero`) + header Kadence transparan (meta `_kad_post_transparent=enable`, set juga di ID 44 saat dipindah).
- **LIVE 26 Okt 2026** di ID 44: konten diganti, `_elementor_edit_mode` dihapus, meta Kadence: fullwidth, judul disembunyikan, unboxed, tanpa padding vertikal, header transparan. Verifikasi render: 200, H1 baru, Yoast title/description utuh, 19 script (sebelumnya Elementor). `_elementor_data` lama disimpan untuk rollback.
- Pratinjau (sudah dibuang ke trash): draft **15606** "Tentang Kami (pratinjau redesain)". Setelah disetujui: `wp_update_page` id 44 dengan isi ini, hapus meta `_elementor_edit_mode`, hapus draft 15606.
- Yoast title/description halaman 44 **tidak diubah** (keputusan SEO no. 2).
