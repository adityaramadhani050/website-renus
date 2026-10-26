# Hubungi Kami (`/hubungi-kami/`, ID 48)

- Isi baru: `hubungi-kami.blocks.html`, dihasilkan `python3 ../pages/build_pages.py hubungi-kami`.
- Sumber lama tetap di meta `_elementor_data` halaman 48 (rollback).
- Perubahan dari versi Elementor:
  - Form Element Pack (`bdt-contact-form`) → **form ke WhatsApp** (Custom HTML + JS kecil): nama & kota wajib, tipe properti, sistem, pesan → membuka `wa.me/6281412250644` dengan pesan terisi. Tidak ada data yang disimpan di server.
  - Kartu WhatsApp per wilayah (Surabaya memakai 0853-8555-8025) → **satu nomor 0814-1225-0644** sesuai CLAUDE.md.
  - Peta widget Elementor → iframe Google Maps `loading="lazy"` per kantor + tautan "Buka di Google Maps".
  - Font Awesome CDN dari HTML lama dibuang (tidak dipakai lagi).
- **LIVE 26 Okt 2026** di ID 48 (draft 15619 dibuang). Render: 200, H1 baru, form ada, 20 script. Meta description Yoast halaman ini masih kosong.
- Setelah disetujui: `wp_update_page` id 48, hapus `_elementor_edit_mode`, set meta Kadence yang sama, buang draft 15619.
