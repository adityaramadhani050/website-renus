# Homepage WordPress (blok Gutenberg)

Sumber kebenaran: `prototypes/landing-plts-hybrid.html`. File di folder ini dihasilkan dari prototipe itu.

| File | Isi |
|---|---|
| `build.py` | Generator. `python3 build.py` → `homepage.blocks.html` + `rn.css`. `--chunks DIR` memecah per section untuk dikirim lewat MCP. |
| `wp-overrides.css` | CSS tambahan khusus WordPress (reset Kadence/core, tombol, gambar, tabel, latest-posts). Diedit manual. |
| `rn.css` | CSS lengkap yang mudah dibaca (prototipe di-scope ke `body .rn` + overrides). |
| `legacy-additional.css` | CSS lama di Additional CSS (sebelum redesain), dipertahankan. |
| `../additional-css.css` | Isi Additional CSS Kadence yang terpasang: CSS lama + `rn.css` versi ringkas. `--inline-css` menaruh CSS di blok HTML sebagai cadangan. |
| `homepage.blocks.html` | Isi halaman (markup blok) yang dikirim ke WordPress. |

## Status (24 Okt 2026) — LIVE
- **Homepage live = halaman 3280** (URL `/` tidak berubah), isi = `homepage.blocks.html` (diverifikasi identik setelah disimpan).
- `_elementor_edit_mode` di 3280 **dihapus** agar WordPress merender blok Gutenberg. `_elementor_data` lama masih tersimpan; untuk rollback: kembalikan meta `_elementor_edit_mode=builder` (atau undo token Royal MCP / revisi halaman).
- CSS di **Additional CSS Kadence** (post 3699) = `wordpress/additional-css.css` (CSS lama + blok `.rn`).
- Yoast 3280: title "Kontraktor PLTS Rumah, Bisnis & Industri - Renus Global Indonesia", description "Pemasangan PLTS on-grid, off-grid, dan hybrid untuk rumah, bisnis, dan industri di seluruh Indonesia. Badan usaha ESDM, 4 sertifikasi ISO, 500+ proyek terpasang."
- Verifikasi render live (1×): status 200, title & description Yoast baru, H1 pertama "Kontraktor PLTS Rumah, Bisnis & Industri", `.rn-home` ada.
- Meta Kadence 3280 (sudah ada): layout fullwidth, judul disembunyikan, unboxed, tanpa padding vertikal.
- Draft uji **15450** "Beranda (redesain)" masih ada (berisi CSS inline) — boleh dihapus.

### Media yang diunggah (2026/10)
| ID | File |
|---|---|
| 15439 / 15440 | hero-plts-hybrid-siang.webp / -hp.webp |
| 15441 / 15442 | hero-plts-hybrid-malam.webp / -hp.webp |
| 15443 / 15444 | hero-plts-hybrid-mendung.webp / -hp.webp |
| 15445 / 15446 | hero-plts-hybrid-pln-padam.webp / -hp.webp |
| 15447 / 15448 / 15449 | isometrik-plts-on-grid / off-grid / hybrid.webp |

Foto proyek & logo klien memakai media lama dengan `wp-image-ID`, sehingga WordPress menambahkan `srcset` otomatis.

## Cara deploy ulang
1. `python3 build.py` → `homepage.blocks.html` dan `../additional-css.css`.
2. CSS berubah → `wp_update_custom_css` dengan isi `wordpress/additional-css.css`.
3. Isi berubah → `wp_update_page` id 3280 dengan `homepage.blocks.html` utuh (satu panggilan), atau `wp_insert_blocks` / `wp_replace_in_page` untuk perubahan kecil. `--chunks DIR` memecah per section bila perlu kirim bertahap.

## Belum dikerjakan
- Menonaktifkan Elementor & addon: **tunggu** halaman 44, 1315, 4120, 3164, 48, 10131 selesai dimigrasi (masih Elementor).
- Font Plus Jakarta Sans masih dimuat dari blok HTML hero; pindahkan ke Typography Kadence saat semua halaman sudah dimigrasi.
- Aktifkan salah satu plugin cache (LiteSpeed/Hummingbird) setelah redesain selesai.
