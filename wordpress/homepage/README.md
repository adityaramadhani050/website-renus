# Homepage WordPress (blok Gutenberg)

Sumber kebenaran: `prototypes/landing-plts-hybrid.html`. File di folder ini dihasilkan dari prototipe itu.

| File | Isi |
|---|---|
| `build.py` | Generator. `python3 build.py` → `homepage.blocks.html` + `rn.css`. `--chunks DIR` memecah per section untuk dikirim lewat MCP. |
| `wp-overrides.css` | CSS tambahan khusus WordPress (reset Kadence/core, tombol, gambar, tabel, latest-posts). Diedit manual. |
| `rn.css` | CSS lengkap (prototipe di-scope ke `body .rn` + overrides). Disisipkan sebagai `<style id="rn-css">` di blok HTML pertama. |
| `homepage.blocks.html` | Isi halaman (markup blok) yang dikirim ke WordPress. |

## Status (24 Okt 2026)
- **Draft**: halaman ID **15450** "Beranda (redesain)" — belum dipublish, homepage live (ID 3280) belum disentuh.
  Edit: https://renergynusantara.com/wp-admin/post.php?post=15450&action=edit
- Meta Kadence disalin dari 3280: `_kad_post_layout=fullwidth`, `_kad_post_title=hide`, `_kad_post_content_style=unboxed`, `_kad_post_vertical_padding=hide`, `_kad_post_feature=hide`. Template: default.
- Verifikasi render (1×, lewat preview): status 200, H1 pertama "Kontraktor PLTS Rumah, Bisnis & Industri", `#rn-css` ada.

### Media yang diunggah (2026/10)
| ID | File |
|---|---|
| 15439 / 15440 | hero-plts-hybrid-siang.webp / -hp.webp |
| 15441 / 15442 | hero-plts-hybrid-malam.webp / -hp.webp |
| 15443 / 15444 | hero-plts-hybrid-mendung.webp / -hp.webp |
| 15445 / 15446 | hero-plts-hybrid-pln-padam.webp / -hp.webp |
| 15447 / 15448 / 15449 | isometrik-plts-on-grid / off-grid / hybrid.webp |

Foto proyek & logo klien memakai media lama dengan `wp-image-ID`, sehingga WordPress menambahkan `srcset` otomatis (mengatasi temuan audit "gambar terlalu besar").

## Cara deploy ulang
1. `python3 build.py --chunks <dir>`
2. `wp_update_page` id 15450 dengan `<dir>/00.html` (wrapper `.rn` + CSS + hero).
3. `wp_insert_blocks` id 15450, `at: inside_end`, `path: "0"` untuk `01.html` … `11.html`, **satu per satu** (shared hosting).

## Belum dikerjakan (perlu keputusan/izin)
- CSS ke Additional CSS: diblokir — aktifkan **Royal MCP → Settings → "Allow AI to modify theme appearance"**. Setelah itu `rn.css` bisa dipindah ke Additional CSS (dipakai ulang di halaman lain) dan `<style id="rn-css">` dihapus dari halaman.
- Menjadikan homepage: salin isi 15450 ke halaman 3280 (slug/URL tetap) lalu ganti Yoast title/description sesuai CLAUDE.md. Belum dilakukan sampai pengguna menyetujui preview.
- Font Plus Jakarta Sans masih dimuat dari blok HTML; idealnya diset di Typography Kadence saat semua halaman sudah dimigrasi.
