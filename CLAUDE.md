# Redesain renergynusantara.com — Konteks Serah-Terima

Dokumen ini berisi konteks dari sesi SEO (22 Oktober 2026) untuk pekerjaan redesain website.
Gunakan Bahasa Indonesia untuk komunikasi dan konten.

## Tujuan redesain
- Lepas Elementor + seluruh addon-nya; bangun ulang halaman dengan **blok Gutenberg (core blocks)** agar bisa dikelola AI lewat MCP.
- Tetap memakai tema **Kadence 1.5.2** (sudah aktif, ramah Gutenberg). Header/footer via header builder Kadence.
- Fokus pesan: **PLTS hybrid + baterai** sebagai kategori utama (sejak Permen ESDM No. 2/2024, kelebihan listrik on-grid yang diekspor tidak lagi mengurangi tagihan).
- Kerjakan di **staging** dulu, baru dipindah ke live.

## Akses
- WordPress 7.1.3, situs: https://renergynusantara.com
- MCP: plugin **Royal MCP** — endpoint `https://renergynusantara.com/wp-json/royal-mcp/v1/mcp` (OAuth). Perlu ditambahkan ulang sebagai connector/MCP server di Claude Code.
- Setiap write Royal MCP memberi undo token 72 jam (Royal MCP → Recent Changes).

## Batasan teknis yang sudah ditemukan
- **Shared hosting, tanpa page cache.** Kerjakan pelan: satu request per waktu, hindari verifikasi render beruntun. Pernah down 503 (penyebab: storage penuh oleh file backup — simpan backup di luar server).
- Widget **ElementsKit** (image-box, icon-box) tidak bisa diedit lewat `elementor_replace_text` → alasan utama pindah ke Gutenberg.
- Meta `_wp_page_template` diproteksi — tidak bisa diubah via MCP (ubah manual di editor).
- `redirection_update_redirect` gagal ("Invalid redirect matcher"); `redirection_create_redirect` berhasil bila `group_id: 1` diisi.
- Plugin cache (LiteSpeed Cache, Hummingbird) terpasang tapi **nonaktif** — aktifkan salah satu setelah redesain.

## Halaman yang perlu dibangun ulang (saat ini Elementor)
| Halaman | ID |
|---|---|
| Homepage (`/`) | 3280 |
| Tentang Kami | 44 |
| Layanan | 1315 |
| Produk | 4120 |
| Proyek | 3164 |
| Hubungi Kami | 48 |
| Artikel (arsip) | 10131 |

Elemen homepage yang wajib dipertahankan/dipindahkan:
- **Kalkulator PLTS** (widget HTML, 4 langkah: tipe properti → konsumsi → kontak → estimasi) → pindah ke blok Custom HTML.
- Logo klien (WIKA, Medco, PUPR, ITS, Perpustakaan Jatim, dll.), galeri proyek, daftar artikel terbaru.
- Popup "Alokasi Kuota Terbatas" (Elementor Pro) → perlu pengganti ringan atau CTA WhatsApp sticky.
- Dua kantor & WhatsApp: Surabaya 0853-8555-8025, Jabodetabek 0814-1225-0644, sales@renergynusantara.com.

Plugin Elementor/addon yang akan dinonaktifkan setelah migrasi: Elementor, Elementor Pro, Element Pack Lite, ElementsKit Lite, Essential Addons, Essential Classy Addons, Premium Addons, Prime Slider, Unlimited Elements, Envato Elements.

## Keputusan SEO yang TIDAK boleh dirusak oleh redesain
1. **Jangan ubah URL/slug** halaman mana pun.
2. **Title & meta description Yoast** sudah diperbarui (jangan ditimpa):
   - Homepage: "Kontraktor PLTS Surabaya & Jabodetabek - Renus Global Indonesia"
   - /pasang-plts/, /biaya-pasang-plts-5000-watt-2026/, /biaya-pasang-plts-2200-watt/, /biaya-pasang-plts-di-surabaya/, /mengenal-pembangkit-listrik-tenaga-surya-plts/, /biaya-plts-on-grid/, /tentang-kami/, /plts-hybrid/, /plts-off-grid/
3. **Homepage harus punya tepat satu H1** berisi kata kunci, mis. "Kontraktor PLTS Surabaya & Jabodetabek" (H1 lama "Renewable Energy Solutions" belum diganti).
4. Angka counter kWh harus tertulis di HTML (bukan hanya animasi JS yang terbaca "0").
5. Kartu Residensial / Komersial / Industrial harus menautkan ke: `/plts-hybrid/`, `/pasang-plts-untuk-bisnis/`, `/plts-industri-manufaktur/`. Tombol "Artikel" → `/artikel/` (bukan Instagram).
6. Deskripsi PLTS On-Grid **tidak boleh** menjanjikan ekspor/kompensasi kelebihan listrik ke PLN.
7. /plts-hybrid/ (ID 394) dan /plts-off-grid/ (ID 372) sudah ditulis ulang sebagai konten Gutenberg biasa dengan H1 di dalam konten (template Elementor Full Width tidak menampilkan judul). Saat ganti template ke default Kadence, **hapus H1 manual di konten** agar tidak dobel.
8. **12 redirect 301** konsolidasi (ID 13–24 di Redirection) + artikel sumbernya di-draft. Jangan dipublish ulang.
9. Atur `lang` situs ke Bahasa Indonesia (saat ini en_US).
10. Gambar: alt text deskriptif, nama file deskriptif, prioritaskan foto proyek asli (bukan gambar AI).

## Harga paket (katalog Agustus 2026, harga material, belum termasuk pemasangan)
- Hybrid 1 phase: 5 kW Rp 84 jt · 6 kW Rp 98 jt · 8 kW Rp 131 jt
- Hybrid 3 phase: 10 kW Rp 159 jt · 12 kW Rp 174 jt · 20 kW Rp 287 jt
- Off-grid VRLA: 1 kW Rp 23 jt · 2 kW Rp 36 jt · 3 kW Rp 49 jt · 5 kW Rp 65 jt
- Off-grid lithium: 5 kW Rp 77 jt · 10 kW Rp 138 jt
- **Jangan tampilkan**: paket off-grid 5 kW + 16 kWh (Rp 92 jt) dan kisaran biaya pemasangan.
- Angka penghematan boleh ditampilkan dengan label estimasi.

## Lainnya
- Subdomain stairlift.renergynusantara.com ikut terindeks dengan konten default ("Hello world") — perlu dirapikan atau di-noindex.
- Sertifikasi untuk trust signals: ISO 9001:2015, badan usaha ESDM DJK.
